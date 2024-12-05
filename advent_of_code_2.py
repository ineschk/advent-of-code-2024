

def is_safe(file_path):
    safe = 0
    reports = []
    # read the file 
    with open(file_path , 'r') as file :

        for report in file :
            report = list(map(int,report.split()))
            reports.append(report)
            # part 1
        '''for report in reports :
            differences = [report[i+1]-report[i] for i in range(len(line)-1)]
            if all(1<=diffrence <= 3 for diffrence in differences):
               safe+=1
            if all(-3<= difference<=-1 for difference in differences):
                safe+=1'''
        
            # part 2
        def check_safe(report):
            # Check if the report is safe without modification (all differences between 1 and 3)
            differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
            if all(1 <= diff <= 3 for diff in differences):
                return True
            # Check if the report is safe with a 1-step increase (all differences between -3 and -1)
            if all(-3 <= diff <= -1 for diff in differences):
                return True
            # Check if the report is safe by removing a single level
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1:]
                modified_differences = [modified_report[j + 1] - modified_report[j] for j in range(len(modified_report) - 1)]
                if all(1 <= diff <= 3 for diff in modified_differences):
                    return True
                if all(-3 <= diff <= -1 for diff in modified_differences):
                    return True
            return False
        def count_safe_reports(reports):
            safe = 0
            for report in reports:
                if check_safe(report):
                    safe += 1
            return safe
        safe = count_safe_reports(reports)


    file.close
    return safe 
                    
                 


# use case : 
file_path = 'input_day_2.txt'
safe_reports = is_safe(file_path)
print(f"Total of safe reports is :{safe_reports}")