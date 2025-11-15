def item_name_to_item_class_name(item_name: str) -> str:
    item_name = item_name.split("__")[0]
    return "".join(word.capitalize() for word in item_name.split("_"))


def all_subclasses(cls):
    subclasses = set(cls.__subclasses__())
    for subclass in cls.__subclasses__():
        subclasses.update(all_subclasses(subclass))
    return subclasses
