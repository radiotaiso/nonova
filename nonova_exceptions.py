
class InvalidProjectException(Exception):
    """
    Raised when the project_id is not in any
    of the get_project returned list of tuples' first
    value (project_id).
    """
    pass

class InvalidCategoryException(Exception):
    """
    Raised when the category_id is not in any
    of get_categories returned list of tuples' first
    value (category_id).
    """

    pass
