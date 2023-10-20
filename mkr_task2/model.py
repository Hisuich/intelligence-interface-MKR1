input_lvs = [
    {
        'X': (0, 101, 1),
        'name': 'ServiceQuality',
        'terms': {
            'Poor': ('trapmf', 0, 0, 25, 37),
            'Fair': ('trapmf', 25, 37, 50, 62),
            'Good': ('trapmf', 50, 62, 75, 87),
            'Excellent': ('trapmf', 75, 87, 100, 100),
        }
    },

    {
        'X': (0, 101, 1),
        'name': 'MealQuality',
        'terms': {
            'Low': ('trapmf', 0, 0, 25, 37),
            'Moderate': ('trapmf', 25, 37, 50, 62),
            'High': ('trapmf', 50, 62, 75, 87),
            'Exceptional': ('trapmf', 75, 87, 100, 100),
        }
    }
]

output_lv = {
    'X': (0, 10.1, 0.1),
    'name': 'Tipsize',
    'terms': {
        'Small': ('trapmf', 0, 0, 1.6, 3.3),
        'Medium': ('trapmf', 1.6, 3.3, 4.9, 6.6),
        'Large': ('trapmf', 4.9, 7.4, 10, 10),
    }
}


rule_base = [
    (('Poor', 'Low'), 'Small'),
    (('Poor', 'Moderate'), 'Small'),
    (('Poor', 'High'), 'Medium'),
    (('Poor', 'Exceptional'), 'Medium'),
    (('Fair', 'Low'), 'Small'),
    (('Fair', 'Moderate'), 'Medium'),
    (('Fair', 'High'), 'Medium'),
    (('Fair', 'Exceptional'), 'Medium'),
    (('Good', 'Low'), 'Medium'),
    (('Good', 'Moderate'), 'Medium'),
    (('Good', 'High'), 'Large'),
    (('Good', 'Exceptional'), 'Large'),
    (('Excellent', 'Low'), 'Medium'),
    (('Excellent', 'Moderate'), 'Medium'),
    (('Excellent', 'High'), 'Large'),
    (('Excellent', 'Exceptional'), 'Large'),
]
