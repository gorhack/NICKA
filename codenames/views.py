from django.http import HttpResponse

# Create your views here.
def index_page(request):
	# TODO:// implement templates
	return HttpResponse("Index...")

def op_detail_page(request, operation_id):
	# TODO:// implement view page by op code
	return HttpResponse("Op #%s" % operation_id)