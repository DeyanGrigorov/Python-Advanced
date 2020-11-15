from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def edit_category(self, category_id: int, new_name: str):
        category_to_edit = list(filter(lambda x: x.id == category_id, self.categories))
        if category_to_edit:
            category_to_edit[0].name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic_to_edit = list(filter(lambda x: x.id == topic_id, self.topics))
        if topic_to_edit:
            topic_to_edit[0].topic = new_topic
            topic_to_edit[0].storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document_to_edit = list(filter(lambda x: x.id == document_id, self.documents))
        if document_to_edit:
            document_to_edit[0].file_name = new_file_name

    def delete_category(self, category_id):
        category_to_del = list(filter(lambda x: x.id == category_id, self.categories))
        if category_to_del:
            self.categories.remove(category_to_del[0])

    def delete_topic(self, topic_id):
        topic_to_del = list(filter(lambda x: x.id == topic_id, self.topics))
        if topic_to_del:
            self.topics.remove(topic_to_del[0])

    def delete_document(self, document_id):
        document_to_del = list(filter(lambda x: x.id == document_id, self.documents))
        if document_to_del:
            self.documents.remove(document_to_del[0])

    def get_document(self, document_id):
        get_doc = list(filter(lambda x: x.id == document_id, self.documents))
        if get_doc:
            return get_doc[0]

    def __repr__(self):
        string_to_return = ''
        for idx, document in enumerate(self.documents):
            if idx != len(self.documents) - 1:
                string_to_return += document.__repr__() + '\n'
            else:
                string_to_return += document.__repr__()
        return string_to_return
