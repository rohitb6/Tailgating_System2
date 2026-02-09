# Gate Entry Approval System - Sample Run

## Scenario 1: Approved Entry

```
============================================================
         GATE ENTRY APPROVAL SYSTEM
============================================================
Welcome to the main gate entry system.
Please follow the instructions below.

------------------------------------------------------------
Enter your name (visitor): Alice Johnson
Enter reason for visit: Meeting with management

------------------------------------------------------------
Available Approvers: John Manager, Sarah Admin, Mike Security, Lisa HR
------------------------------------------------------------
Enter name of the approver: John Manager

============================================================
APPROVAL REQUEST TO: John Manager
============================================================
Visitor Name: Alice Johnson
Reason for Visit: Meeting with management
------------------------------------------------------------
Approve this entry? (yes/no): yes

✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ 
🔓 GATE OPENED - ACCESS GRANTED
✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ 
Welcome! Please proceed through the gate.

------------------------------------------------------------
📋 ACCESS LOG RECORD:
------------------------------------------------------------
Visitor: Alice Johnson
Reason: Meeting with management
Approver: John Manager
Status: APPROVED
------------------------------------------------------------

Process another entry? (yes/no): no

============================================================
Thank you for using Gate Entry Approval System!
============================================================
```

---

## Scenario 2: Rejected Entry

```
============================================================
         GATE ENTRY APPROVAL SYSTEM
============================================================
Welcome to the main gate entry system.
Please follow the instructions below.

------------------------------------------------------------
Enter your name (visitor): Bob Smith
Enter reason for visit: Delivery

------------------------------------------------------------
Available Approvers: John Manager, Sarah Admin, Mike Security, Lisa HR
------------------------------------------------------------
Enter name of the approver: Mike Security

============================================================
APPROVAL REQUEST TO: Mike Security
============================================================
Visitor Name: Bob Smith
Reason for Visit: Delivery
------------------------------------------------------------
Approve this entry? (yes/no): no

❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ 
🔒 GATE CLOSED - ACCESS DENIED
❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ 
Your entry request was denied. Please contact administration.

------------------------------------------------------------
📋 ACCESS LOG RECORD:
------------------------------------------------------------
Visitor: Bob Smith
Reason: Delivery
Approver: Mike Security
Status: REJECTED
------------------------------------------------------------

Process another entry? (yes/no): no
```

---

## Scenario 3: Unauthorized Approver

```
------------------------------------------------------------
Enter your name (visitor): Carol Davis
Enter reason for visit: Inspection

------------------------------------------------------------
Available Approvers: John Manager, Sarah Admin, Mike Security, Lisa HR
------------------------------------------------------------
Enter name of the approver: Unknown Person

❌ Error: Approver not found in system!
'Unknown Person' is not an authorized approver.

------------------------------------------------------------
📋 ACCESS LOG RECORD:
------------------------------------------------------------
Visitor: Carol Davis
Reason: Inspection
Approver: Unknown Person
Status: DENIED
------------------------------------------------------------

❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ 
🔒 GATE CLOSED - ACCESS DENIED
❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ ❌ 
Your entry request was denied. Please contact administration.

Process another entry? (yes/no): no
```

---

## Key Features Demonstrated

✅ **Step-by-step process**: Collects visitor info → Gets approver name → Validates approver → Requests decision  
✅ **Error handling**: Validates empty inputs and non-existent approvers  
✅ **Case-insensitive matching**: "john manager" works same as "John Manager"  
✅ **Access logging**: Records all entries with decision  
✅ **Clear visual feedback**: Using ✅/❌ emojis and sections  
✅ **Loop support**: Process multiple visitors in one session
