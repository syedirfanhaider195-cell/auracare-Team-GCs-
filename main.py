# AuraCare Health System Core

APP_VERSION = "2.0.0-Beta"
MODULES_ENABLED = []


def patient_triage(patient_name, severity):
    return f"{patient_name} has triage severity: {severity}"

def doctor_schedule(doctor_name):
    return f"Schedule found for Dr. {doctor_name}"