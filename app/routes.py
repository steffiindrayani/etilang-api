from app import app, db, crawler

from app.models import ETilang
from app.schema import etilang_schema

from flask import request, jsonify, make_response

@app.route("/api/etilang/check", methods=["POST"])
def check_etilang():
    data = {
        "plate": request.json['plate_number'],
        "machineNumber": request.json['machine_number'],
        "skeletonNumber": request.json['skeleton_number'],
    }
    result = crawler.get_tilang_info(data)

    if not result:
        response = {
            'message': 'ETilang not found',
            'status': 404,
        }
        return make_response(jsonify(response))

    new_etilang = ETilang(
            plate_number=result.plate_number, machine_number=result.machine_number,
            skeleton_number=result.skeleton_number, location=result.location,
            offense_type=result.offense_type, status=result.status,
            offense_timestamp=result.offense_timestamp, crawl_timestamp=result.crawl_timestamp,
    )
    db.session.add(new_etilang)
    db.session.commit()
    result = etilang_schema.dump(new_etilang)
    data = {
        'message': 'ETilang found',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data))
