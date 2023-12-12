commit;

alter table f12023_raceresults_race
add column Round integer first;

update f12023_raceresults_race
set Round = 1
where track = "Bahrain";

update f12023_raceresults_race
set Round = 2
where track = "Saudi Arabia";

update f12023_raceresults_race
set Round = 3
where track = "Australia";

update f12023_raceresults_race
set Round = 4
where track = "Azerbaijan";

update f12023_raceresults_race
set Round = 5
where track = "Miami";

update f12023_raceresults_race
set Round = 6
where track = "Monaco";

update f12023_raceresults_race
set Round = 7
where track = "Spain";

update f12023_raceresults_race
set Round = 8
where track = "Canada";

update f12023_raceresults_race
set Round = 9
where track = "Austria";

update f12023_raceresults_race
set Round = 10
where track = "Great Britain";

update f12023_raceresults_race
set Round = 11
where track = "Hungary";

update f12023_raceresults_race
set Round = 12
where track = "Belgium";

update f12023_raceresults_race
set Round = 13
where track = "Netherlands";

update f12023_raceresults_race
set Round = 14
where track = "Italy";

update f12023_raceresults_race
set Round = 15
where track = "Singapore";

update f12023_raceresults_race
set Round = 16
where track = "Japan";

update f12023_raceresults_race
set Round = 17
where track = "Qatar";

update f12023_raceresults_race
set Round = 18
where track = "United States";

update f12023_raceresults_race
set Round = 19
where track = "Mexico";

update f12023_raceresults_race
set Round = 20
where track = "Brazil";

update f12023_raceresults_race
set Round = 21
where track = "Las Vegas";

update f12023_raceresults_race
set Round = 22
where track = "Abu Dhabi";

alter table f12023_raceresults_race
add primary key (Round);

select * from f12023_raceresults_race
order by round;