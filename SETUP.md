# Gate Entry Approval System - Web Version with Email Integration

## 📋 Overview

This is a web-based Gate Entry Approval System that allows:
- **Visitors** to request office access via a web form
- **Approvers** to approve/reject requests via email links
- **Admin** to view all access requests in a dashboard

## ✨ Features

✅ **Visitor Request Form** - Beautiful web interface to request access  
✅ **Email-Based Approvals** - Approvers get email with one-click approval/rejection links  
✅ **Admin Dashboard** - View all requests with real-time status updates  
✅ **Request Tracking** - Track status of each request  
✅ **Beautiful UI** - Modern, responsive design  

---

## 🚀 Installation & Setup

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Configure Email Settings

Edit `app.py` and update these values:

```python
SMTP_SERVER = "smtp.gmail.com"          # Your email provider's SMTP server
SMTP_PORT = 587
SENDER_EMAIL = "your-email@gmail.com"   # Your email address
SENDER_PASSWORD = "your-app-password"   # Your app-specific password
```

**For Gmail:**
1. Enable 2-factor authentication
2. Create an "App Password" at https://myaccount.google.com/apppasswords
3. Use that password in `SENDER_PASSWORD`

**For Other Providers:**
- Gmail: smtp.gmail.com:587
- Outlook: smtp-mail.outlook.com:587
- Yahoo: smtp.mail.yahoo.com:465
- Custom: Use your company's SMTP settings

### 3. Run the Application

```bash
python app.py
```

The system will start on `http://localhost:5000`

---

## 📱 User Flow

### For Visitors:

1. Open `http://localhost:5000`
2. Fill in your details:
   - Name
   - Email
   - Reason for visit
   - Select approver from list
3. Click "Send Approval Request"
4. Approver receives email with approval link
5. Check dashboard to see request status

### For Approvers:

1. Receive email from the system
2. Click "APPROVE ACCESS" or "REJECT ACCESS" button
3. Confirmation page shows the decision
4. System records the decision

### For Admins:

1. Visit `http://localhost:5000/dashboard`
2. View all access requests
3. See real-time statistics
4. Track approval status

---

## 📧 Email Template Example

Approvers receive a professional HTML email with:
- Visitor name and reason
- One-click approval button (green)
- One-click rejection button (red)
- Unique secure token for each request

---

## 🔧 Configuration Options

### Adding/Removing Approvers

Edit the `AUTHORIZED_APPROVERS` dictionary in `app.py`:

```python
AUTHORIZED_APPROVERS = {
    "John Manager": "john@company.com",
    "Sarah Admin": "sarah@company.com",
    "New Person": "newperson@company.com"  # Add like this
}
```

### Security Token Settings

The system automatically generates secure tokens. To customize expiration:
- Current: 24-hour expiration (can be modified in code)
- Each request gets unique token
- Tokens are stored in memory (use database for production)

---

## 📊 Data Storage

**Current Version (Development):**
- In-memory storage (data lost on restart)
- Good for testing and demos

**For Production:**
- Replace with SQLite, PostgreSQL, or MongoDB
- Store in `access_requests` table
- Implement proper logging

---

## 🔒 Security Considerations

✅ **Current Implementation:**
- Unique tokens for each approval request
- Email-based approvals (approver identity verification)
- Request logging

**For Production, Add:**
- Database encryption
- SSL/TLS for web interface
- User authentication for admin dashboard
- CSRF token protection
- Rate limiting
- Audit logs

---

## 📂 File Structure

```
Tailgating/
├── app.py                           # Main Flask application
├── requirements.txt                 # Python dependencies
├── gate_entry_system.py             # Original console version
├── SETUP.md                         # This file
└── templates/
    ├── index.html                   # Visitor request form
    ├── dashboard.html               # Admin dashboard
    ├── approval_response.html        # Approval confirmation page
    ├── error.html                   # Error page
    └── approval_error.html          # Expired link error page
```

---

## 🐛 Troubleshooting

### Email Not Sending?

1. Check `SENDER_EMAIL` and `SENDER_PASSWORD` are correct
2. Verify SMTP server and port are correct for your email provider
3. Check if 2-factor authentication is enabled (may need app password)
4. Check firewall/antivirus blocking SMTP

### Port Already in Use?

```bash
python app.py --port 5001  # Use different port
```

### Template Not Found?

Ensure `templates/` folder exists with all HTML files

---

## 🎯 Next Steps / Enhancements

- [ ] Add database support (SQLite/PostgreSQL)
- [ ] Implement user authentication
- [ ] Add SMS notifications
- [ ] Integrate with RFID readers
- [ ] Hardware gate control (GPIO)
- [ ] Email verification
- [ ] Request history export
- [ ] Mobile app
- [ ] Integration with building access systems

---

## 📄 License

Free to use and modify for your organization.

---

## 💡 Support

For issues or questions:
1. Check the troubleshooting section
2. Verify email configuration
3. Check Flask debug output for error messages
