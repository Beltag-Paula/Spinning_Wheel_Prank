import pygame
import math
import sys
import time
import pranks
from message_idiot import MessageIdiot
import os

justAPrankBro = pranks.Pranks()

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinning Wheel")
clock = pygame.time.Clock()

# Wheel properties
wheel_center = (WIDTH // 2, HEIGHT // 2)
wheel_radius = 250
num_segments = 8
segment_angle = 360 / num_segments
colors = ["#880000", "#884400", "#888800", "#008800", "#008888", "#000088", "#440088", "#880088"]
labels = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Font setup
font = pygame.font.SysFont(None, 24)

# Spinning control
start_angle = 0
spinning = False
speed = 0


def draw_wheel(start_angle):
    screen.fill((255, 255, 255))  # White background

    # Draw each segment
    for i in range(num_segments):
        # Calculate angles in radians
        start_rad = math.radians(start_angle + i * segment_angle)
        end_rad = math.radians(start_angle + (i + 1) * segment_angle)

        # Define polygon points for the segment
        points = [wheel_center,
                  (wheel_center[0] + wheel_radius * math.cos(start_rad),
                   wheel_center[1] + wheel_radius * math.sin(start_rad)),
                  (wheel_center[0] + wheel_radius * math.cos(end_rad),
                   wheel_center[1] + wheel_radius * math.sin(end_rad))]

        # Draw the segment
        pygame.draw.polygon(screen, pygame.Color(colors[i]), points)

        # Calculate text position (center of the segment arc)
        mid_angle = math.radians(start_angle + (i + 0.5) * segment_angle)
        text_x = wheel_center[0] + (wheel_radius - 50) * math.cos(mid_angle)
        text_y = wheel_center[1] + (wheel_radius - 50) * math.sin(mid_angle)

        # Render and draw the text
        text_surface = font.render(labels[i], True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(text_x, text_y))
        screen.blit(text_surface, text_rect)

    # Draw the triangle indicator at the top
    triangle_size = 20
    triangle_color = (0, 0, 0)  # Black color
    triangle_offset = 20
    triangle_points = [
        (wheel_center[0] + wheel_radius + triangle_offset, wheel_center[1]),  # Tip of the triangle
        (wheel_center[0] + wheel_radius + triangle_size + triangle_offset, wheel_center[1] - triangle_size),
        (wheel_center[0] + wheel_radius + triangle_size + triangle_offset, wheel_center[1] + triangle_size)
    ]
    pygame.draw.polygon(screen, triangle_color, triangle_points)

    pygame.display.flip()


def get_prize(start_angle):
    normalized_angle = start_angle % 360
    winning_segment = int((360 - normalized_angle) / segment_angle) % num_segments
    return labels[winning_segment]


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not spinning:
            spinning = True
            speed = 30  # Initial speed; [6,4,2,7,2,8]

    if spinning:
        start_angle += speed
        if speed > 0:
            speed -= 0.2  # Deceleration
        else:
            speed = 0
            spinning = False
            prize = get_prize(start_angle)
            print(f"Congratulations! You won {prize}")
            if prize == '1':
                print("")
            if prize == '2':
                justAPrankBro.create_prank_windows(30)
                # Wait for the prank windows to close
                time.sleep(5)  # Adjust this if needed
            if prize == '3':
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                num_folders = 2  # Change this number to create more or fewer folders
                # virtual machine  "C:/Users/kali/PycharmProjects/pythonProject/assets/icon_malware.ico"
                icon_path = "C:/Users/Paula/PycharmProjects/SpinningWheel/assets/icon_malware.ico"
                justAPrankBro.create_folders(desktop_path, num_folders, icon_path=icon_path)
                time.sleep(3)
                justAPrankBro.delete_folders(desktop_path, num_folders)
            if prize == '4':
                justAPrankBro.rotate_screen()
            if prize == '5':
                # virtual machine "C:/Users/kali/PycharmProjects/pythonProject/assets/hell_1.mp4"
                video_path = "C:/Users/Paula/PycharmProjects/SpinningWheel/assets/hell_1.mp4"
                justAPrankBro.play_video_fullscreen(video_path)
            if prize == '6':
                justAPrankBro.open_youtube_video_with_delay("https://www.youtube.com/watch?v=BBGEG21CGo0", 5, 2)
            if prize == '7':
                print("")
                message_idiot = MessageIdiot()
                message_idiot.run()
            if prize == "8":
                break

    draw_wheel(start_angle)
    clock.tick(30)
