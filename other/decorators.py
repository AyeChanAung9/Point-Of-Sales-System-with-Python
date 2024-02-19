from functools import wraps
from flask import session, redirect, url_for, Response
from typing import Callable, Any, Union, Tuple, Literal


def login_required(view_func: Callable[..., Union[str, Response, dict[str, Any], Tuple[Response, Literal[200]], Tuple[Response, Literal[400]], Any]]) -> Callable[..., Union[str, Response, dict[str, Any], Tuple[Response, Literal[200]], Tuple[Response, Literal[400]], Any]]:
    @wraps(view_func)
    def wrapped_view(*args: Any, **kwargs: Any) -> Union[str, Response, dict[str, Any], Tuple[Response, Literal[200]], Tuple[Response, Literal[400]], Any]:
        if not session.get('logged_in', False):
            # Redirect to the login page if the user is not authenticated.
            return redirect(url_for('index'))
        return view_func(*args, **kwargs)
    return wrapped_view
