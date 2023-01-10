# Web application – Team Rzułte Papaje

## Team members
Role | Name | TUL Identificator | GH login
--- | --- | --- | ---
tester | Justyna Owczarek | 229301 | jowczar
devops | Bartłomiej Ołubek | 229300 | ShanghaiG
dev1 | Robert Dudziński | 229248 | Dudzinski-Robert
dev2 | Cezary Karczewski | 229268 | ckarczewski
dev3 | Artur Szydłowski | 229322 | Artur229322
scrum master | Justyna Owczarek | 229301 | jowczar

## Tools & technologies 
Area | Tools & technologies
--- | ---
Backend | Python – Django
Frontend | TypeScript – ReactJS
Database | PostgreSQL
Hosting + CI + CD | Vercel + GitHub
Project management | Jira
Team communication | Discord + Teams

## Project management
Backlog, roadmap, estimates, issues, kanban of active sprint and sprint reports are available on Jira [here](https://politechnika.atlassian.net/jira/software/c/projects/ZPI/boards/1). You can also find the burndown chart for each sprint here.
<br>
### Understanding client needs
The team conducted two sprint meetings with the customer/Product Owner, determining the functional and non-functional requirements of the system. The result of these meetings is a [document available here](./RzultePapierze_zalozenia-v4.pdf).
<br><br>
This was followed by a separate team meeting, estimating workloads, creating a roadmap with an approximate release schedule and defining user stories in the Jira tool.
<br>
### Team meetings
The team conducts weekly sprints. Retrospectives, estimation of the next sprint and task selection take place at meetings on Mondays. Since team members have varying working hours and are available mostly during the evenings, "daily" meetings to remove obstacles are held as needed.
<br>

## Workflows & CI/CD
The chosen system to ensure continuous integration is [Vercel](https://vercel.com).
<br>
Vercel is a fast-growing platform that enables deployment at every step of a project. It ensures that all changes in the repository are automatically built and deployed to the server. Vercel is fully integrated with GitHub. if a build fails, Vercel sends an email about it, it also includes this information in the Pull Request if the changes have been exposed for review. This makes it possible to react quickly to errors and fix them. No change will be implemented if the build breaks. Changes will be automatically rolled back by Vercel to the latest working version, so a working application is always ensured for users.
<br>
### Hosting
With Vercel, we do not have to worry about hosting our application, as it is provided in the free version of the account. Additionally, each change gets its preview on Vercel so that the person working on a feature can share a link to the change on the server before it is accepted to the target branch of the code. This means the person reviewing the change does not have to run a local server – just click on the link and preview the changes in the browser.
<br>
### Configuration values
Vercel is offered in a serverless model and requires no special configuration - other than granting access to the repository, selecting the root directory (in our case, the backend and frontend are 2 separate projects on Vercel) and possibly setting other parameters (in our case, Vercel's default values were sufficient). In addition to these settings, you also had to supply environment variables, the same process as values placed in the [local .env files](#building-this-project-on-local-system).
<br>
### Access
Due to the public visibility of this repository, Vercel account data will be made available at the request of the Product Owner - via a private channel.
<br>
### Continuous Testing
Two additional GitHub workflows have been introduced that take care of test execution.
Their configuration is available in [directory .github/workflows](./.github/workflows/). For a Pull Request to be accepted, all tests and a successful build from Vercel must be passed.
<br>
### Production
The production version of the application (branch main) can be viewed [here](https://zpi-2022-zaoczni-rzulte-papaje.vercel.app/).
<br>

## Building this project on the local system
TBD by developers