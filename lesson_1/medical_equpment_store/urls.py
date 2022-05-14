from datetime import date
from views import Index, Contact


# front controller
def secret_front(request):
    request['date'] = date.today()


fronts = [secret_front]

routes = {
    '/': Index(),
    '/contact/': Contact(),
}
