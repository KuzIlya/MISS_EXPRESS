from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import serializers

from mssite import mixins as ms_mixins
from product_components import models as product_components_models
from product_components import serializers as product_components_serializers

from . import fields, mixins, models


class ProductSizeSerializer(serializers.ModelSerializer):

    id = serializers.PrimaryKeyRelatedField(
        read_only=True,
        source='size'
    )

    name = serializers.SlugRelatedField(
        source='size',
        slug_field='name',
        queryset=product_components_models.Size.objects.all()
    )

    class Meta:
        model = models.ProductSize
        fields = [
            'id',
            'name',
            'amount'
        ]


class ProductColorSerializer(serializers.ModelSerializer):

    id = serializers.PrimaryKeyRelatedField(
        read_only=True,
        source='color'
    )

    slug = serializers.SlugRelatedField(
        source='color',
        slug_field='slug',
        queryset=product_components_models.Color.objects.all()
    )

    color = serializers.SlugRelatedField(
        read_only=True,
        slug_field='color'
    )

    class Meta:
        model = models.ProductColor
        fields = [
            'id',
            'slug',
            'color',
            'amount'
        ]


class ProductBaseSerializer(
    ms_mixins.BaseLocalizationMixin,
    TranslatableModelSerializer
):

    colors_data = ProductColorSerializer(
        source='colors',
        many=True
    )

    sizes_data = ProductSizeSerializer(
        source='sizes',
        many=True
    )

    manufacturerCountry = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=product_components_models.ManufacturerCountry.objects.all()
    )

    images = serializers.ListSerializer(
        child=fields.Base64ImageField()
    )

    brand = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        translated_fields = [
            'mold',
            'season'
        ]

    def get_brand(self, obj):
        return obj.provider.company


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        exclude = [
            'product'
        ]


class ProductCreateSerializer(
    mixins.ProductMixin,
    ProductBaseSerializer
):

    name = serializers.CharField(
        required=False,
        trim_whitespace=True
    )

    description = serializers.CharField(
        required=False,
        trim_whitespace=True
    )

    compound = serializers.CharField(
        required=False,
        trim_whitespace=True
    )

    pattern = serializers.CharField(
        required=False,
        trim_whitespace=True
    )

    class Meta(ProductBaseSerializer.Meta):
        exclude = [
            'color',
            'size',
            'article_number',
            'is_famous',
            'provider'
        ]


class ProductUpdateSerializer(
    mixins.ProductMixin,
    ProductBaseSerializer
):

    name = serializers.CharField(
        required=False,
        trim_whitespace=True
    )

    description = serializers.CharField(
        required=False,
        trim_whitespace=True
    )

    compound = serializers.CharField(
        required=False,
        trim_whitespace=True
    )

    pattern = serializers.CharField(
        required=False,
        trim_whitespace=True
    )

    class Meta(ProductBaseSerializer.Meta):
        exclude = [
            'color',
            'size',
            'article_number',
            'category',
            'is_famous',
            'provider'
        ]


class ProductSerializer(
    ms_mixins.TranslatedSerializerMixin,
    ProductBaseSerializer
):

    translations = TranslatedFieldsField(
        shared_model=models.Product
    )

    category = product_components_serializers.CategoriesSerializer()

    class Meta(ProductBaseSerializer.Meta):
        model = models.Product
        exclude = [
            'size',
            'color'
        ]


class ProductOrderSerializer(
    ms_mixins.TranslatedSerializerMixin,
    TranslatableModelSerializer
):

    translations = TranslatedFieldsField(
        shared_model=models.Product
    )

    images = ImageSerializer(
        many=True
    )

    class Meta:
        model = models.Product
        fields = [
            'id',
            'translations',
            'images',
            'article_number',
            'price'
        ]
        read_only_fields = [
            'translations'
        ]


class ProductDataArchiveSerializer(
    ms_mixins.TranslatedSerializerMixin,
    TranslatableModelSerializer
):

    translations = TranslatedFieldsField(
        shared_model=models.Product
    )

    class Meta:
        model = models.Product
        fields = [
            'translations',
            'article_number'
        ]
        read_only_fields = [
            'translations'
        ]


class ProductStatusChangeArchiveSerializer(
    serializers.ModelSerializer
):

    product = ProductDataArchiveSerializer()

    class Meta:
        model = models.ProductStatusChangeArchive
        fields = '__all__'
