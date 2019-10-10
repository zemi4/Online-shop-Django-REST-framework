from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Product, Category


@registry.register_document
class ProductsDocument(Document):
    category = fields.ObjectField(properties={
        'name': fields.TextField(),
    })

    class Index:
        # Name of the Elasticsearch index
        name = 'products'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Product  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',
            'description'
        ]
        related_models = [Category]

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Category):
            return related_instance.category.all()
