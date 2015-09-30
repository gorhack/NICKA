from django.http import HttpResponse

# Create your views here.
def index_page(request):
	return HttpResponse("hello world")

def op_detail_page(request, operation_id):
	return HttpResponse("Op #%s" % operation_id)