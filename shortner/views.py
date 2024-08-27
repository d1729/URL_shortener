from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from shortner.serializers import ShortUrlSerializer
from shortner.services import generate_unique_short_code, get_original_url, get_url_object, check_short_url


class ShortenerView(APIView):
    def post(self, request):
        data = request.data
        original_url = data['original_url']
        data['short_code'] = generate_unique_short_code()
        serializer = ShortUrlSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, shortcode):
        original_url = get_original_url(shortcode)
        if not original_url:
            return Response({'message': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'original_url': original_url}, status=status.HTTP_308_PERMANENT_REDIRECT)


    def delete(self, request, shortcode):
        url = get_url_object(shortcode)
        if not url:
            return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)
        url.delete()
        return Response({'message': 'Success'}, status=status.HTTP_204_NO_CONTENT)


    def patch(self, request):
        data = request.data
        original_shortcode = data['original_shortcode']

        url = get_url_object(original_shortcode)
        if not url:
            return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)

        new_shortcode = data['new_shortcode']
        new_shortcode_exists = check_short_url(new_shortcode)
        if new_shortcode_exists:
            return Response({'error': 'New shortcode already exists'}, status=status.HTTP_400_BAD_REQUEST)

        url.short_code = new_shortcode

        url.save()
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
