"""
Gate Entry Approval System with Email & Web Interface
Integrates email-based approvals and provides a web interface
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import secrets
import os

# ============================================================================
# CONFIGURATION
# ============================================================================

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

# Authorized approvers with email addresses
AUTHORIZED_APPROVERS = {
    "Rohit": "rohitbarik48@gmail.com",
    "Swadhinjit": "swadhinjitshoo@gmail.com",
    "Pritam": "creedskull747@gmail.com",
    "Lisa HR": "lisa@company.com"
}

# Email configuration (update with your SMTP details)
SMTP_SERVER = "smtp.gmail.com"  # Change for your email provider
SMTP_PORT = 587
SENDER_EMAIL = "loginai760@gmail.com"  # Your email - UPDATE THIS
SENDER_PASSWORD = "owikzupqgabcfoqb"  # Your app password - UPDATE THIS

# In-memory storage for access requests (use database in production)
access_requests = {}
approval_tokens = {}

# ============================================================================
# EMAIL FUNCTIONS
# ============================================================================

def send_approval_email(visitor_name, visitor_reason, approver_name, approver_email, approval_token):
    """
    Send email to approver with approval/rejection links
    """
    try:
        # Create unique approval and rejection links
        approval_link = f"http://localhost:5000/approve/{approval_token}?action=approve"
        rejection_link = f"http://localhost:5000/approve/{approval_token}?action=reject"
        
        # Create email message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"Gate Entry Approval Request - {visitor_name}"
        msg['From'] = SENDER_EMAIL
        msg['To'] = approver_email
        
        # HTML email body
        html = f"""\
        <html>
          <body style="font-family: Arial, sans-serif; background-color: #f4f4f4;">
            <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
              <h2 style="color: #333; border-bottom: 3px solid #007bff; padding-bottom: 10px;">Gate Entry Approval Request</h2>
              
              <div style="background-color: #f9f9f9; padding: 15px; border-left: 4px solid #007bff; margin: 20px 0;">
                <p><strong>Visitor Name:</strong> {visitor_name}</p>
                <p><strong>Reason for Visit:</strong> {visitor_reason}</p>
                <p><strong>Request Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
              </div>
              
              <p>Please approve or reject this access request by clicking the buttons below:</p>
              
              <div style="text-align: center; margin: 30px 0;">
                <a href="{approval_link}" style="display: inline-block; background-color: #28a745; color: white; padding: 12px 30px; text-decoration: none; border-radius: 5px; margin-right: 10px; font-weight: bold;">✅ APPROVE ACCESS</a>
                <a href="{rejection_link}" style="display: inline-block; background-color: #dc3545; color: white; padding: 12px 30px; text-decoration: none; border-radius: 5px; font-weight: bold;">❌ REJECT ACCESS</a>
              </div>
              
              <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">
              <p style="color: #666; font-size: 12px;">This link expires in 24 hours. This is an automated message from Gate Entry System.</p>
            </div>
          </body>
        </html>
        """
        
        msg.attach(MIMEText(html, 'html'))
        
        # Send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


# ============================================================================
# ROUTES
# ============================================================================

@app.route('/')
def index():
    """Homepage - Visitor request form"""
    approvers = list(AUTHORIZED_APPROVERS.keys())
    return render_template('index.html', approvers=approvers)


@app.route('/check-status-page')
def check_status_page():
    """Check status page - visitor can check their request status"""
    return render_template('check_status.html')


@app.route('/request-access', methods=['POST'])
def request_access():
    """Handle visitor access request"""
    data = request.json
    
    visitor_name = data.get('visitor_name', '').strip()
    visitor_email = data.get('visitor_email', '').strip()
    reason = data.get('reason', '').strip()
    approver_name = data.get('approver_name', '').strip()
    photo_data = data.get('photo_data', None)
    
    # Validation
    if not all([visitor_name, visitor_email, reason, approver_name]):
        return jsonify({'success': False, 'message': 'All fields are required'}), 400
    
    if not photo_data:
        return jsonify({'success': False, 'message': 'Photo is required'}), 400
    
    # Check if approver exists
    if approver_name not in AUTHORIZED_APPROVERS:
        return jsonify({'success': False, 'message': 'Approver not found in system'}), 400
    
    # Create unique token for this request
    request_token = secrets.token_urlsafe(32)
    approver_email = AUTHORIZED_APPROVERS[approver_name]
    
    # Store request details
    access_requests[request_token] = {
        'visitor_name': visitor_name,
        'visitor_email': visitor_email,
        'reason': reason,
        'approver_name': approver_name,
        'status': 'pending',
        'timestamp': datetime.now(),
        'photo_data': photo_data
    }
    
    approval_tokens[request_token] = approver_name
    
    # Send approval email
    email_sent = send_approval_email(visitor_name, reason, approver_name, approver_email, request_token)
    
    if email_sent:
        return jsonify({
            'success': True,
            'message': f'Approval request sent to {approver_name} via email',
            'request_id': request_token
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to send email. Please try again.'
        }), 500


@app.route('/check-status/<request_id>')
def check_status(request_id):
    """Check status of access request - Show beautiful status page"""
    if request_id not in access_requests:
        return render_template('status_display.html', 
                             success=False, 
                             request_id=request_id,
                             message='Request not found or has expired')
    
    request_data = access_requests[request_id]
    return render_template('status_display.html',
                         success=True,
                         request_id=request_id,
                         status=request_data['status'],
                         visitor_name=request_data['visitor_name'],
                         approver_name=request_data['approver_name'],
                         timestamp=request_data['timestamp'].isoformat())


@app.route('/api/check-status/<request_id>')
def api_check_status(request_id):
    """API endpoint for checking status (returns JSON)"""
    if request_id not in access_requests:
        return jsonify({'success': False, 'message': 'Request not found'}), 404
    
    request_data = access_requests[request_id]
    return jsonify({
        'success': True,
        'status': request_data['status'],
        'visitor_name': request_data['visitor_name'],
        'approver_name': request_data['approver_name'],
        'timestamp': request_data['timestamp'].isoformat()
    })


@app.route('/photo/<request_id>')
def get_photo(request_id):
    """Get photo for a request"""
    if request_id not in access_requests:
        return jsonify({'success': False, 'message': 'Request not found'}), 404
    
    request_data = access_requests[request_id]
    photo_data = request_data.get('photo_data')
    
    if not photo_data:
        return jsonify({'success': False, 'message': 'No photo available'}), 404
    
    # Return the base64 photo data
    return jsonify({
        'success': True,
        'photo_data': photo_data,
        'visitor_name': request_data['visitor_name']
    })


@app.route('/approve/<token>')
def approve_request(token):
    """Email approval/rejection link handler"""
    action = request.args.get('action', 'approve')
    
    if token not in access_requests:
        return render_template('approval_error.html', message='Request not found or has expired')
    
    request_data = access_requests[token]
    
    if action == 'approve':
        request_data['status'] = 'approved'
        message = f"✅ Access APPROVED for {request_data['visitor_name']}"
        color = 'green'
    else:
        request_data['status'] = 'rejected'
        message = f"❌ Access REJECTED for {request_data['visitor_name']}"
        color = 'red'
    
    return render_template('approval_response.html', 
                         message=message, 
                         color=color,
                         visitor_name=request_data['visitor_name'],
                         approver_name=request_data['approver_name'])


@app.route('/dashboard')
def dashboard():
    """Admin dashboard to view all requests"""
    requests_list = []
    for token, req in access_requests.items():
        requests_list.append({
            'id': token[:16] + '...',
            'visitor': req['visitor_name'],
            'approver': req['approver_name'],
            'reason': req['reason'],
            'status': req['status'],
            'time': req['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
        })
    
    return render_template('dashboard.html', requests=requests_list)


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', message='Page not found'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('error.html', message='Server error occurred'), 500


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    print("\n" + "="*60)
    print("Gate Entry Approval System - Web Interface")
    print("="*60)
    print("Starting Flask application...")
    print("Visit: http://localhost:5000")
    print("\n⚠️  IMPORTANT: Configure email settings in app.py first!")
    print("="*60 + "\n")
    
    app.run(debug=True, port=5000)
