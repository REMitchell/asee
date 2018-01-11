# asee

This was written for Python 3.6 and not tested with other Python versions

Install two Python libraries:
- BeautifulSoup (pip install bs4)
- Requests (pip install requests)

To run, modify the search term (currently 'culture') passed to the <code>startSearch</code> function on the last line of the script. 

```$ python crawler.py```

This will search for your search term and start printing out the title and abstract of all found articles to the terminal. 

Sample Output:

```
Retrieving URL:
https://peer.asee.org/advanced_search?collection_id=&page=1&published_after=&published_before=&q=culture&q_in%5B%5D=title&q_in%5B%5D=content&year=
Retrieving URL:
https://peer.asee.org//cultural-competency-assessment

---------------------------------

TITLE IS:
Cultural Competency Assessment
ABSTRACT IS:



Abstract
NOTE:  The first page of text has been automatically extracted and included below in lieu of an abstract


                            Cultural Competency Assessment
Abstract
Cultural competency is defined as the ability to effectively interact with people from diverse
cultures and recognize the importance of cultural differences. These skills will be increasingly
important for environmental engineers who work on teams with professionals from diverse
backgrounds and design solutions to global problems. For example, these skills are particularly
important when engaging in projects for Engineers Without Borders (EWB) and similar
organizations. In order to evaluate if curriculum help develop these skills in students, an
assessment instrument is needed. A wide variety of such surveys have been developed and
validated, although generally for settings outside engineering academia. In this research, the
Miville-Guzman Universality-Diversity Scale short form (MGUDS-S) was used. It is a written
15 question survey with responses on a 6-point Likert scale. It evaluates universal-diverse
orientation (UDO) and has been most widely used in medical school settings. The overall UDO
score is composed of three subscales: diversity of contact, relativistic appreciation, and
discomfort with differences. The author also added four of the Pittsburgh Freshman Engineering
Attitudes Survey (PFEAS) questions and eight self-created questions to the survey, in addition to
```

Areas for improvement:
- Collecting additional information about the articles, such as authors and citations
- Removing the "Abstract" title, and potentially "notes" subtitle from abstract text
- Better exception handling. No exceptions were encountered during test run, but you may experience a timeout, bad HTTP code, or oddly formatted link/article page that breaks things. In this case, you may want to ignore the faulty article (log it?) and continue searching.
