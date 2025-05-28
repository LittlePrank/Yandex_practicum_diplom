# Дарья Плотникова, 30-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def get_track_number_order():
    track_number = sender_stand_request.post_new_order()
    return track_number.json()['track']

def test_receive_order_by_order_tracking():
    track_number = get_track_number_order()
    response = sender_stand_request.get_order_by_numder(track_number)
    assert response.status_code == 200