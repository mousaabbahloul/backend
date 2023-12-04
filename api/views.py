from rest_framework.response import Response
from rest_framework.decorators import api_view
from .prediction import load_model
from PIL import Image

@api_view(["POST", "GET"])
def start(request):
    print("ffffffffffffffffffffff")
    return Response({"response": "starting"})


@api_view(["POST", "GET"])
def index(request):
    print("ffffffffffffffffffffff")
    if request.method == "POST":
        if 'input_file' in request.FILES:
            input_file = request.FILES['input_file']
            image = Image.open(input_file)
            # image = image_preprocess(image)
            pr = load_model(image)

            # get_data(image)
            print(pr)
    return Response(pr)
