from prototype.models import Incident


class RiskEngine:
    """
    Calculates a risk score for a correlated incident.
    """

    def calculate(self, incident: Incident):

        score = 0

        # --------------------------
        # Severity Score (40)
        # --------------------------

        severity_scores = {
            "Low": 10,
            "Medium": 25,
            "High": 40,
            "Critical": 40,
        }

        score += severity_scores.get(incident.severity, 0)

        # --------------------------
        # Confidence Score (30)
        # --------------------------

        score += int(incident.confidence * 30)

        # --------------------------
        # Event Count Score (30)
        # --------------------------

        score += min(incident.event_count * 10, 30)

        # --------------------------
        # Risk Level
        # --------------------------

        if score >= 80:
            level = "Critical"

        elif score >= 60:
            level = "High"

        elif score >= 40:
            level = "Medium"

        else:
            level = "Low"

        return {
            "score": score,
            "level": level,
        }
