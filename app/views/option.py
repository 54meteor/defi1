import importlib
import inspect
from hobbit_core.db import EnumExt

from flask import Blueprint, jsonify


bp = Blueprint('option', __name__)


@bp.route('/options/', methods=['GET'])
def option():
    return jsonify({
        name: obj.to_opts(verbose=True)
        for name, obj in importlib.import_module(
            'app.models.consts').__dict__.items()
        if inspect.isclass(obj) and issubclass(obj, EnumExt) and obj != EnumExt
    })
