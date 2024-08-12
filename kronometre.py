import time

def kronometre():
    lap_times = []
    total_start = time.time()
    input("Kronometreyi başlatmak için Enter'a basın. Her tur zamanını kaydetmek için Enter'a basmaya devam edin. Bitirmek için 'q' girin.")

    while True:
        start_time = time.time()
        response = input("Yeni tur için Enter'a basın veya bitirmek için 'q' girin: ")
        if response.lower() == 'q':
            break
        end_time = time.time()
        lap_time = end_time - start_time
        lap_times.append(lap_time)
        print(f"{len(lap_times)}. tur süresi: {lap_time:.2f} saniye")

    total_end = time.time()
    total_elapsed = total_end - total_start
    print("\nTurların Zamanları:")
    for index, lap in enumerate(lap_times, 1):
        print(f"{index}. Tur: {lap:.2f} saniye")
    print(f"Toplam geçen süre: {total_elapsed:.2f} saniye")

kronometre()
