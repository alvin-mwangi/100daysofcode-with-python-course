from functools import wraps


def make_html(element):
    """Decorator to wrap html tags"""
    def make_html(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # call the decorated function
            result = func(*args, **kwargs)
            result = f"<{element}>{result}</{element}>"
            return result
        return wrapper
    return make_html

@make_html("test2")
@make_html("test")
def make_text(text):
    return text

print(make_text("test string"))


