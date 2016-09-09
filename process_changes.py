# CA3 - Perform Analytics on a 5000 entry dataset
# Module - Programming for Big Data
# Student - Galina Lopez 10333429

changes_file = 'changes_python.txt'

# open the file - and read all of the lines.
# use strip to strip out spaces and trim the line.
data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

sep = 72*'-'

# create the commit class to hold each of the elements
class Commit(object):
    'class for commits'
    # initialising default constructor
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)

# create the statistic class to hold statistic subsets: authors, changes, dates and days in dictionaries
class Statistic(object):
    'class for statistics'
    # initialising default constructor
    def __init__(self):    
        self.authors = {}       
        self.dates = {}
        self.times = {}
        self.days = {}
        self.changes = {}
            
    # adding get length to my statistic 
    def get_length(self, dictionary):
        return len(dictionary)
        
    # adding get highest value to my statistic
    def get_highest(self, dictionary):
        return max([[v,k] for k,v in dictionary.items()])
        
    # adding get lowest value to my statistic    
    def get_lowest(self, dictionary):
        return min([[v,k] for k,v in dictionary.items()])
        
    # adding perform averages to my statistic
    def get_average(self, dictionary, total):
        avg_dictionary = {}
        for k,v in dictionary.items():
            avg_dictionary[k] = float('%.2f' %(v/float(total)))
        return avg_dictionary
        
# print results to the screen    
def print_results(dictionary):
    for k,v in dictionary.items():
        print v, '\t', k        

# sort and print results to the screen        
def print_sorted_results(dictionary):
    print 'Sorted'
    list = []
    for k,v in dictionary.items():
        list.append((v,k))
    list.sort(reverse = True)
    for v,k in list:        
        print v, '\t', k
    #in one line of code
    #print sorted([[v,k] for k,v in dictionary.items()])
    
# performs basic analysis of the statistical subset
def basic_analysis(statistic, statistic_subset, subset_type):

    # display subset
    print '\nCommits\t', subset_type
    print_results(statistic_subset) 
    
    # find subset length
    print '\n', subset_type + 's :', statistic.get_length(statistic_subset)
    
    # display subset in ascending order of values
    print '\nCommits\t', subset_type
    print_sorted_results(statistic_subset)
       
    # find highest value
    highest = statistic.get_highest(statistic_subset)
    print '\nHighest', subset_type +':', highest[1], 'with', highest[0], 'commits'
    
    # find lowest value
    lowest = statistic.get_lowest(statistic_subset)
    print '\nLowest', subset_type +':', lowest[1], 'with', lowest[0], 'commits'
        
    # find the average per day
    number_of_dates = statistic.get_length(statistic.dates)
    
    # display subset in ascending order of values
    print '\nAverage per day'
    print 'Commits\t',subset_type
    print_sorted_results(statistic.get_average(statistic_subset,number_of_dates))        
        
statistic = Statistic()
commits = []
current_commit = None
index = 0
while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip() 
        # keep stats of the authors and their number of occurrences
        statistic.authors[current_commit.author] = statistic.authors.get(current_commit.author, 0) + 1
        current_commit.date = details[2].strip()
        # keep stats of the dates and their number of occurrences
        date = details[2].strip().split(' ')[0]
        statistic.dates[date] = statistic.dates.get(date, 0) + 1
        # keep stats of the times of day and their number of occurrences
        time = details[2].strip().split(' ')[1]
        hour = int(time.strip().split(':')[0])
        minute = int(time.strip().split(':')[1])
        second = int(time.strip().split(':')[2])
        if hour < 12: statistic.times['morning'] = statistic.times.get('morning', 0) + 1 
        else: statistic.times['afternoon'] = statistic.times.get('afternoon', 0) + 1 
        # keep stats of the days of the week and their number of occurrences
        day = details[2].strip().split(' ')[3].lstrip('(').split(',')[0]
        statistic.days[day] = statistic.days.get(day, 0) + 1        
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index + 2 : data.index('', index + 1)]
        # keep stats of the types of changes and their number of occurrences
        i = 3        
        for change in data[index + 3 : data.index('', index + 1)]:
            key = data[index + i].strip().split(' ')[0]          
            statistic.changes[key] = statistic.changes.get(key, 0) + 1
            i += 1       
        index = data.index('', index + 1)
        current_commit.comment = data[index + current_commit.comment_line_count:index]
        commits.append(current_commit)
        index = data.index(sep, index + current_commit.comment_line_count)
        
    except IndexError:
        break

# print the number of commit objects
print(len(commits))

commits.reverse()
    
# perform basic analysis
# of authors
basic_analysis(statistic, statistic.authors, 'Author')
# of days of the week
basic_analysis(statistic, statistic.days, 'Day')
# of type of changes
basic_analysis(statistic, statistic.changes, 'Change')
# of times of the day
basic_analysis(statistic, statistic.times, 'Time')

