from django.http import JsonResponse
from deepface import DeepFace

def recognise_face(request):
    if request.method == 'POST' and 'image' in request.FILES:
        file = request.FILES['image']
        img = file.read()

        try:
            # Perform face recognition
            result = DeepFace.verify(img1_path="path/to/known_face.jpg", img2=img)
            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'No file found or incorrect request method'})
