import re

def evaluate_report(i_report):
    if i_report == sorted(i_report) or i_report == sorted(i_report, reverse=True):
        for i in range(0, len(i_report)-1):
            if abs(i_report[i] - i_report[i+1]) <= 3 and abs(i_report[i] - i_report[i+1]) >= 1:
                if i == len(i_report)-2:
                    return True
                continue
            else:
                break
        
    return False

with open('input.txt', 'r') as f:
    data = [a.split(' ') for a in f.readlines()]

print(f'\nPART 1:')
safe = 0
bad_reports = []
for report in data:
    i_report = [int(a.strip()) for a in report]
    if evaluate_report(i_report):
        safe += 1
    else:
        bad_reports.append(i_report)

print(safe)

print(f'\nPART 2: {len(bad_reports)} Bad reports.')
for report in bad_reports:
    for i in range(0, len(report)):
        new_report = report.copy()
        new_report.pop(i)
        
        if evaluate_report(new_report):
            safe += 1
            break
        else:
            continue
        
print(safe)