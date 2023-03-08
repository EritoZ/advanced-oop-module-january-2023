from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        try:
            category_object: Category = next(filter(lambda c: c.id == category_id, self.categories))

            category_object.edit(new_name)

        except StopIteration:
            pass

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        try:
            topic_object: Topic = next(filter(lambda t: t.id == topic_id, self.topics))

            topic_object.edit(new_topic, new_storage_folder)

        except StopIteration:
            pass

    def edit_document(self, document_id: int, new_file_name: str):
        try:
            document_object: Document = next(filter(lambda d: d.id == document_id, self.documents))

            document_object.edit(new_file_name)

        except StopIteration:
            pass

    def delete_category(self, category_id):
        [self.categories.remove(category) for category in self.categories if category.id == category_id]

    def delete_topic(self, topic_id):
        [self.topics.remove(topic) for topic in self.topics if topic.id == topic_id]

    def delete_document(self, document_id):
        [self.documents.remove(document) for document in self.documents if document.id == document_id]

    def get_document(self, document_id):
        try:
            document_object: Document = next(filter(lambda d: d.id == document_id, self.documents))

            return document_object

        except StopIteration:
            pass

    def __repr__(self):
        documents = [str(document) for document in self.documents]

        return '\n'.join(documents)
    