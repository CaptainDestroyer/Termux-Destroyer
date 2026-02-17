import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, ID3NoHeaderError

def update_metadata(file_path, report_file):
    try:
        audio = MP3(file_path, ID3=ID3)
    except ID3NoHeaderError:
        audio = MP3(file_path)
        audio.add_tags()
    
    tags_changed = False
    log_messages = []
    
    # Target specific files
    if file_path == "Access-Granted.mp3":
        # Force update Artist
        audio.tags.add(TPE1(encoding=3, text="Destroyer"))
        log_messages.append(f"Forced Artist update to 'Destroyer' for {file_path}")
        tags_changed = True

        # Force update Title
        audio.tags.add(TIT2(encoding=3, text="KURAMA System Operated Sound"))
        log_messages.append(f"Forced Title update to 'KURAMA System Operated Sound' for {file_path}")
        
    elif file_path in ["KURAMA.mp3", "Naruto.mp3"]:
        # Force update Artist
        audio.tags.add(TPE1(encoding=3, text="Destroyer"))
        log_messages.append(f"Forced Artist update to 'Destroyer' for {file_path}")
        tags_changed = True

        # Force update Title
        audio.tags.add(TIT2(encoding=3, text="KURAMA system operation sound"))
        log_messages.append(f"Forced Title update to 'KURAMA system operation sound' for {file_path}")
    
    if tags_changed:
        audio.save()
        log_messages.append(f"Saved changes for {file_path}")
    else:
        log_messages.append(f"No changes needed for {file_path}")

    # Verify changes
    audio = MP3(file_path, ID3=ID3)
    verification = [
        f"File: {file_path}",
        f"  Artist: {audio.tags.get('TPE1')}",
        f"  Title: {audio.tags.get('TIT2')}",
        "-" * 20
    ]
    
    full_log = "\n".join(log_messages + verification)
    print(full_log)
    report_file.write(full_log + "\n")

with open("report.txt", "w", encoding="utf-8") as f:
    files = [file for file in os.listdir('.') if file.endswith('.mp3')]
    for file in files:
        update_metadata(file, f)
