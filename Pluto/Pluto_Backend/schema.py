import graphene
from graphene_django import DjangoObjectType, DjangoListField

from .models import *

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email", "bio", "timestamp", "friends", "profile_picture")

class MessageType(DjangoObjectType):
    class Meta:
        model = Message
        fields = ("id", "author", "content", "reply", "timestamp")

class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        fields = ("owner", "name" ,"description", "group_icon", "admins", "members", "timestamp")
    
class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_messages = graphene.List(MessageType)
    all_groups_of_user = graphene.List(GroupType, member=graphene.String())
    user = graphene.Field(UserType, id=graphene.Int(), username=graphene.String(), email=graphene.String())
    message = graphene.Field(MessageType, id=graphene.Int())
    group = graphene.Field(GroupType, id=graphene.Int())

    def resolve_all_users(root, info): return User.objects.all()
    def resolve_all_messages(root, info): return Message.objects.all()
    def resolve_all_groups_of_user(root, info, member):
        if member == "currentUser": member = info.context.user.username 
        member = User.objects.get(username=member)
        groups = Group.objects.filter(members=member)
        groups = groups.order_by("-timestamp").all()
        return groups
    def resolve_user(root, info, id=None, username=None, email=None): 
        if id: return User.objects.get(id=id)
        if username: return User.objects.get(username=username)
        if email: return User.objects.get(email=email)
        return None
    def resolve_message(root, info, id):
        if id: return Message.objects.get(id=id)
        return None
    def resolve_group(root, info, id=None):
        if id: return Group.objects.get(id=id)
        return None
    
    
schema = graphene.Schema(query=Query)   