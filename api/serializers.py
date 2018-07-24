from rest_framework import serializers
from restaurants.models import Restaurant
# from django.contrib.auth import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'first_name', 'last_name']

class RestaurantListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = 'api-detail',
        lookup_field = 'id',
        lookup_url_kwarg = 'restaurant_id'
    )
    # owner = serializers.SerializerMethodField()
    detail1 = serializers.HyperlinkedIdentityField(
        view_name = 'api-update',
        lookup_field = 'id',
        lookup_url_kwarg = 'restaurant_id'
    )
    detail2 = serializers.HyperlinkedIdentityField(
        view_name = 'api-delete',
        lookup_field = 'id',
        lookup_url_kwarg = 'restaurant_id'
    )

    class Meta:
        model = Restaurant
        fields = [
            'name',
            'opening_time',
            'closing_time',
            'detail',
            'detail1',
            'detail2'
            ]
    # def get_created_by(self,obj):
    #     return obj.owner.user


class RestaurantDetailSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = 'api-update',
        lookup_field = 'id',
        lookup_url_kwarg = 'restaurant_id'
    )
    detail1 = serializers.HyperlinkedIdentityField(
        view_name = 'api-delete',
        lookup_field = 'id',
        lookup_url_kwarg = 'restaurant_id'
    )
    class Meta:
        model = Restaurant
        fields = [
            'id',
            'owner',
            'name',
            'description',
            'opening_time',
            'closing_time',
            'detail',
            'detail1'
            ]

class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'description',
            'opening_time',
            'closing_time',
            ]
