from django.forms import widgets
from rest_framework import serializers
from questionbank.models import Questions, Category, QUESTION_TYPES

class CategoryListSerializer(serializers.Field):
    def to_internal_value(self, data):
        if type(data) is not list:
            raise ParseError("expected a list of data")
        return [Category.objects.get_or_create(name=c)[0] for c in data]

    def to_representation(self, obj):
        if type(obj) is not list:
            return [tag.name for tag in obj.all()]
        return obj

class QuestionSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only=False)
    class Meta:
        model = Questions
        fields = ('id', 'question', 'category', 'question_type', 'solution')
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        try:
            category_data = validated_data.pop('category')
        except:
            category_data = []
        ques = Questions.objects.create(**validated_data)
        ques.category = category_data
        ques.save()
        return ques

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.question = validated_data.get('question', instance.question)
        instance.category = validated_data.get('category', instance.category.all())
        instance.question_type = validated_data.get('question_type', instance.question_type)
        instance.solution = validated_data.get('solution', instance.solution)
        instance.save()
        return instance


