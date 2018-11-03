from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

  links = serializers.SerializerMethodField(source='get_links')

  class Meta:
    model = User
    fields = (User.USERNAME_FIELD,
      'first_name', 'last_name', 'other_name',
      'japanese_address', 'japanese_billing_address',
      'hungarian_billing_address', 'hungarian_address',
      'is_active', 'links'
    )

  def get_links(self, obj):
    request = self.context['request']
    username = obj.get_username()
    return {
        'self': reverse('user-detail', kwargs={User.USERNAME_FIELD: username}, request=request)
    }
