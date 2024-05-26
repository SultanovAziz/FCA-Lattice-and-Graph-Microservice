from flask import jsonify, current_app
from . import main_bp

@main_bp.route('/')
def index():
    return jsonify({"message": "Welcome Aiz!"})

@main_bp.route('/routes', methods=['GET'])
def list_routes():
    try:
        import urllib
        output = []
        for rule in current_app.url_map.iter_rules():
            methods = ','.join(rule.methods)
            line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
            output.append(line)
        return jsonify(output)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
