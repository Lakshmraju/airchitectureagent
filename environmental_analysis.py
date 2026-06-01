class EnvironmentalAnalyzer:

    def __init__(self, orientation, wind_direction, road_side):
        self.orientation = orientation
        self.wind_direction = wind_direction
        self.road_side = road_side

    def analyze_sunlight(self):
        sunlight = {
            "North": "Moderate sunlight throughout the day",
            "South": "High sunlight exposure",
            "East": "Good morning sunlight",
            "West": "Strong afternoon sunlight"
        }
        return sunlight.get(self.orientation, "Unknown orientation")

    def analyze_ventilation(self):
        if self.orientation == self.wind_direction:
            return "Excellent natural ventilation"
        elif self.orientation in ["East", "West"]:
            return "Good cross ventilation"
        else:
            return "Moderate ventilation"

    def analyze_accessibility(self):
        road_scores = {
            "North": 8,
            "South": 7,
            "East": 9,
            "West": 7
        }

        score = road_scores.get(self.road_side, 5)

        if score >= 8:
            return "Excellent road accessibility"
        elif score >= 6:
            return "Good road accessibility"
        else:
            return "Limited road accessibility"

    def calculate_suitability_score(self):
        score = 0

        if self.orientation == "East":
            score += 30
        elif self.orientation == "North":
            score += 25
        else:
            score += 20

        if self.wind_direction == self.orientation:
            score += 30
        else:
            score += 20

        if self.road_side == "East":
            score += 20
        else:
            score += 15

        return score

    def generate_report(self):
        report = {
            "Sunlight Analysis": self.analyze_sunlight(),
            "Ventilation Analysis": self.analyze_ventilation(),
            "Accessibility Analysis": self.analyze_accessibility(),
            "Suitability Score": self.calculate_suitability_score()
        }

        return report


# Example Usage

if __name__ == "__main__":

    analyzer = EnvironmentalAnalyzer(
        orientation="East",
        wind_direction="East",
        road_side="East"
    )

    report = analyzer.generate_report()

    print("\nENVIRONMENTAL ANALYSIS REPORT")
    print("-" * 40)

    for key, value in report.items():
        print(f"{key}: {value}")