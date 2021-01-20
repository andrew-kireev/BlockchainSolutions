from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, InvalidPage
import requests, json
from app.models import Blocks, BlocksManager


# Create your views here.

def test(request):
    print(request)

    result = requests.get('https://bcschain.info/api/blocks')
    json_response = result.json()
    print(len(json_response))
    print(json_response[0])
    # map = json.loads(json_response)
    # print(map[0:2])

    return render(request, 'all_blocks.html')


def paginate(objects_list, request):
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    paginator = Paginator(objects_list, 50)
    if paginator.num_pages == 0:
        return None, None
    try:
        page = paginator.page(page_number)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    except InvalidPage:
        page = paginator.page(1)

    return page.object_list, page


def get_all_blocks(request):
    blocks = Blocks.objects.all()
    blocks = list(reversed(blocks))
    page_obj, page = paginate(blocks, request)

    return render(request, 'all_blocks.html', {
        'blocks': page_obj,
        'page': page
    })


def one_block(request, block_height):
    block = BlocksManager().get_one_bloc(int(block_height))

    return render(request, 'one_block.html', {
        'block': block
    })
