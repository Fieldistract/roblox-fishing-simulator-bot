from utils.screen import capture_screen
import time


class BubbleDetector:
    def __init__(self):
        self.last_detection_time = 0
        self.detection_cooldown = 2.0  # Cooldown in seconds

    def check_air_bubbles_on_screen(self):
        """Check for air bubbles with cooldown to prevent multiple detections"""
        bubblecolor1 = (68, 252, 234)
        bubblecolorlava = (68, 252, 234)
        bubblecolorvoid = (68, 252, 234)
        current_time = time.time()
        if current_time - self.last_detection_time < self.detection_cooldown:
            return False

        try:
            bits, screen_width, screen_height = capture_screen()

            chunk_size = 50
            matches_found = False

            for y in range(0, screen_height - chunk_size, chunk_size):
                if matches_found:
                    break
                for x in range(0, screen_width - chunk_size, chunk_size):
                    matches = 0
                    for sample_y in range(y, y + chunk_size, 2):
                        for sample_x in range(x, x + chunk_size, 2):
                            pixel_offset = (sample_y * screen_width + sample_x) * 4
                            if pixel_offset + 2 >= len(bits):
                                continue

                            b = bits[pixel_offset]
                            g = bits[pixel_offset + 1]
                            r = bits[pixel_offset + 2]

                            if (
                                abs(r - 68) < 2
                                and abs(g - 252) < 2
                                and abs(b - 234) < 2
                            ):
                                matches += 1

                            if matches >= 3:
                                self.last_detection_time = current_time
                                return True

            return False

        except Exception as e:
            print(f"Error checking bubbles: {e}")
            return False
