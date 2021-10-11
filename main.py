from connectpyse.company import companies_api
from connectpyse.system import members_api
from connectpyse.procurement import purchase_order_line_item_api
from connectpyse.service import ticket_notes_api, ticket_note, tickets_api, ticket, ticket_task, boards_api

#URL = 'https://aus.myconnectwise.net/v2020_3/apis/3.0'

URL = 'https://api-aus.myconnectwise.net/v4_6_release/apis/3.0'

AUTH = {'Authorization': 'Basic YW5kbW9yKzd5aXpVbHBJWjFPeDU0cXk6DWHBaY0hhUVdvcg==',
        'clientId': 'de1b7590-9214-473b-b844-0c80d7b570'}
m = members_api.MembersAPI(url=URL, auth=AUTH)
a_member = m.get_members_count()
print(a_member)

list_comp = companies_api.CompaniesAPI(url=URL, auth=AUTH)
all_company = list_comp.get_companies()
for oneAct in all_company:
 print(oneAct.identifier)


lineItems = purchase_order_line_item_api.PurchaseOrderLineItemAPI(url=URL, auth=AUTH, parent=1)
myItems = lineItems.get_purchase_order_line_items()
print(myItems)

ticket_notes = ticket_notes_api.TicketNotesAPI(url=URL, auth=AUTH, ticket_id=35783)
note = ticket_note.TicketNote({"text": "testing ticket note update.. ", "detailDescriptionFlag": True})
######note2 = ticket_note
ticket_notes.create_ticket_note(note)

boards = boards_api.BoardsAPI(url=URL, auth=AUTH)
all_boards = boards.get_boards()
for b in all_boards:
 print(b.name)


tick = tickets_api.TicketsAPI(url=URL, auth=AUTH)
all_tickets = tick.get_tickets_count()
print(all_tickets)
##new_ticket = ticket.Ticket({"id": 35976, "board": boards.get_board_by_id(1), "status": 16, "company": 250, "summary": "compassib.com.au expiry in 19 days"})
#####create_ticket({"board": "Support Board", "status": "new", "company": "TG Financial Pty Ltd", "summary": "DNS expiry in 15 days"})
##tick.create_ticket(new_ticket)

comp = companies_api.CompaniesAPI(url=URL, auth=AUTH)
all_company = comp.get_companies()
print(all_company)
for c in all_company:
     print(c.name)
