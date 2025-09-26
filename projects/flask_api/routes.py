from flask import Blueprint, jsonify, request

bp = Blueprint('api', __name__)

@bp.route('/health')
def health():
    return jsonify(status='ok')

@bp.route('/echo')
def echo():
    msg = request.args.get('msg', '')
    return jsonify(message=msg)

@bp.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json(silent=True) or {}
    nums = data.get('nums', [])
    try:
        total = sum(float(x) for x in nums)
    except (TypeError, ValueError):
        return jsonify(error='nums must be a list of numbers'), 400
    return jsonify(total=total)
