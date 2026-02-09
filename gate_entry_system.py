"""
Gate Entry Approval System
A simple console-based system that manages gate access through approvers.
Easily extensible for hardware integration (GPIO, RFID readers, etc.)
"""

# ============================================================================
# CONFIGURATION - Easy to extend and modify
# ============================================================================

# List of authorized approvers in the system
AUTHORIZED_APPROVERS = [
    "John Manager",
    "Sarah Admin",
    "Mike Security",
    "Lisa HR"
]

# ============================================================================
# MAIN SYSTEM FUNCTIONS
# ============================================================================

def display_welcome():
    """Display welcome message and system info"""
    print("\n" + "="*60)
    print("         GATE ENTRY APPROVAL SYSTEM")
    print("="*60)
    print("Welcome to the main gate entry system.")
    print("Please follow the instructions below.\n")


def get_visitor_info():
    """Collect visitor information"""
    print("-" * 60)
    visitor_name = input("Enter your name (visitor): ").strip()
    reason = input("Enter reason for visit: ").strip()
    
    if not visitor_name or not reason:
        print("❌ Error: Name and reason cannot be empty!")
        return None
    
    return {"name": visitor_name, "reason": reason}


def get_approver_name():
    """Get the approver name from visitor"""
    print("\n" + "-" * 60)
    print(f"Available Approvers: {', '.join(AUTHORIZED_APPROVERS)}")
    print("-" * 60)
    approver_name = input("Enter name of the approver: ").strip()
    
    return approver_name


def verify_approver(approver_name):
    """
    Check if approver exists in authorized list
    Returns: True if valid, False otherwise
    """
    # Case-insensitive comparison for better UX
    return any(approver.lower() == approver_name.lower() 
               for approver in AUTHORIZED_APPROVERS)


def request_approval(visitor_info, approver_name):
    """
    Ask approver for approval or rejection
    Returns: "approved" or "rejected"
    """
    print("\n" + "="*60)
    print(f"APPROVAL REQUEST TO: {approver_name}")
    print("="*60)
    print(f"Visitor Name: {visitor_info['name']}")
    print(f"Reason for Visit: {visitor_info['reason']}")
    print("-" * 60)
    
    # Simulate approver decision
    while True:
        decision = input("Approve this entry? (yes/no): ").strip().lower()
        
        if decision in ["yes", "y"]:
            return "approved"
        elif decision in ["no", "n"]:
            return "rejected"
        else:
            print("❌ Invalid input. Please enter 'yes' or 'no'.")


def open_gate():
    """Simulate opening the gate"""
    print("\n" + "✅ "*20)
    print("🔓 GATE OPENED - ACCESS GRANTED")
    print("✅ "*20)
    print("Welcome! Please proceed through the gate.\n")


def close_gate():
    """Simulate closing/blocking the gate"""
    print("\n" + "❌ "*20)
    print("🔒 GATE CLOSED - ACCESS DENIED")
    print("❌ "*20)
    print("Your entry request was denied. Please contact administration.\n")


def log_access_record(visitor_info, approver_name, status):
    """
    Log the access attempt (can be extended to write to file/database)
    """
    print("\n" + "-" * 60)
    print("📋 ACCESS LOG RECORD:")
    print("-" * 60)
    print(f"Visitor: {visitor_info['name']}")
    print(f"Reason: {visitor_info['reason']}")
    print(f"Approver: {approver_name}")
    print(f"Status: {status.upper()}")
    print("-" * 60 + "\n")


def process_entry():
    """
    Main process flow for gate entry
    Orchestrates all steps
    """
    display_welcome()
    
    # Step 1: Get visitor information
    visitor_info = get_visitor_info()
    if not visitor_info:
        return
    
    # Step 2: Get approver name
    approver_name = get_approver_name()
    
    # Step 3: Verify if approver is authorized
    if not verify_approver(approver_name):
        print("\n❌ Error: Approver not found in system!")
        print(f"'{approver_name}' is not an authorized approver.")
        log_access_record(visitor_info, approver_name, "denied")
        close_gate()
        return
    
    # Step 4: Request approval from the approver
    decision = request_approval(visitor_info, approver_name)
    
    # Step 5: Process the decision
    if decision == "approved":
        open_gate()
        log_access_record(visitor_info, approver_name, "approved")
    else:
        close_gate()
        log_access_record(visitor_info, approver_name, "rejected")


def run_system():
    """Main system loop - allows multiple entries"""
    while True:
        process_entry()
        
        # Ask if another visitor wants to enter
        another = input("Process another entry? (yes/no): ").strip().lower()
        if another not in ["yes", "y"]:
            print("\n" + "="*60)
            print("Thank you for using Gate Entry Approval System!")
            print("="*60 + "\n")
            break


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    run_system()
