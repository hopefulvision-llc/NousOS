import time
import random
from datetime import datetime

# Physiological/emotional states (unchanged)
HEART_RATE_STATES = {
    "resting_calm":       (62,  4,   "Deep relaxation / meditation"),
    "normal_awake":       (72,  5,   "Everyday relaxed but awake"),
    "focused_work":       (85,  7,   "Concentrated work / mild stress"),
    "moderate_exercise":  (125, 12,  "Brisk walking / light cardio"),
    "intense_exercise":   (165, 18,  "Running / HIIT peak"),
    "stress_anxiety":     (110, 15,  "Acute stress / anxiety attack"),
    "fear_panic":         (140, 22,  "Strong fear or panic response"),
    "excitement_joy":     (115, 14,  "Very excited / thrilled"),
    "anger_frustration":  (128, 18,  "Strong anger or frustration")
}

# All modifiers: substances + meds + NEW environmental/physiological ones!
MODIFIERS = {
    # Previous substances
    "coffee":          (15,   5,   "Caffeine boost - increased alertness"),
    "alcohol":         (10,   10,  "Alcohol - mild euphoria with irregularity"),
    "weed_sativa":     (20,   8,   "Sativa weed - energizing and uplifting"),
    "weed_indica":     (-10,  3,   "Indica weed - relaxing and sedative"),
    "nicotine":        (12,   6,   "Nicotine hit - quick stimulant effect"),
    "adrenaline":      (30,   15,  "Adrenaline rush - fight-or-flight spike"),
    
    # Medications
    "med_adhd_stimulant":   (12,   8,   "ADHD stimulant (e.g., Adderall) - increased alertness & BPM"),
    "med_beta_blocker":     (-15, -5,   "Beta-blocker (e.g., metoprolol) - slows heart rate & reduces variability"),
    "med_decongestant":     (10,   6,   "Pseudoephedrine (cold med) - mild stimulant effect"),
    "med_bronchodilator":   (18,  10,  "Albuterol (asthma) - quick BPM spike"),
    "med_thyroid":          (15,   7,   "Levothyroxine (thyroid) - increases BPM if high dose"),
    
    # NEW: Environmental & physiological factors
    "hot_environment":      (12,   8,   "Hot weather/humidity - cardiovascular strain for cooling"),
    "cold_environment":     (5,    4,   "Cold exposure - mild vasoconstriction response"),
    "dehydration":          (15,  10,  "Dehydration - reduced blood volume, heart works harder"),
    "high_altitude":        (20,  12,  "Acute high altitude - hypoxia drives sympathetic increase"),
    "deep_breathing":       (-10, -6,  "Slow/deep breathing - parasympathetic activation, calms HR"),
    
    "none":            (0,    0,   "No modifier")
}

def simulate_heart_rate(state_name="normal_awake", modifier_name="none", duration_seconds=60):
    """
    Simulate heart rate for a state + optional modifier.
    Prints log every ~1 second.
    """
    if state_name not in HEART_RATE_STATES:
        print(f"Unknown state '{state_name}'. Available:")
        for s in HEART_RATE_STATES:
            print(f"  - {s:18} → {HEART_RATE_STATES[s][2]}")
        return
    
    if modifier_name not in MODIFIERS:
        print(f"Unknown modifier '{modifier_name}'. Available:")
        for m in MODIFIERS:
            if m != "none":
                print(f"  - {m:25} → {MODIFIERS[m][2]}")
        return
    
    # Get base from state
    base_bpm, variability, state_desc = HEART_RATE_STATES[state_name]
    
    # Apply modifier deltas
    bpm_delta, var_delta, mod_desc = MODIFIERS[modifier_name]
    mod_base_bpm = base_bpm + bpm_delta
    mod_variability = max(2, variability + var_delta)  # Keep variability reasonable
    
    print(f"\nStarting simulation: {state_desc}")
    if modifier_name != "none":
        print(f"Modifier: {modifier_name} ({mod_desc})")
    print(f"Adjusted Base BPM: {mod_base_bpm} • Adjusted Variability: ±{mod_variability}")
    print("-" * 85)
    print("Timestamp              BPM   State                  Modifier")
    print("-" * 85)
    
    start_time = time.time()
    
    while time.time() - start_time < duration_seconds:
        fluctuation = random.gauss(0, mod_variability)
        slow_drift = random.uniform(-1.5, 1.5)
        
        current_bpm = mod_base_bpm + fluctuation + slow_drift
        current_bpm = max(45, min(195, round(current_bpm)))  # Realistic bounds
        
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mod_display = modifier_name if modifier_name != "none" else "-"
        print(f"{now}    {current_bpm:3d}   {state_name:20}   {mod_display}")
        
        time.sleep(random.uniform(0.85, 1.15))

    print("-" * 85)
    print("Simulation finished.\n")


# ────────────────────────────────────────────────────────────────
# Examples - uncomment to test (mix & match!)
# ────────────────────────────────────────────────────────────────

# simulate_heart_rate("normal_awake", "hot_environment", 45)           # Hot day baseline
# simulate_heart_rate("moderate_exercise", "dehydration", 60)         # Workout while dehydrated
simulate_heart_rate("stress_anxiety", "high_altitude", 40)            # Anxiety at altitude
# simulate_heart_rate("resting_calm", "deep_breathing", 30)           # Relaxation via breathing
# simulate_heart_rate("intense_exercise", "cold_environment", 50)     # Cold-weather workout
