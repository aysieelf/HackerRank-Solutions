/*
Task:
    Given a date string, dateString, in the format MM/DD/YYYY, find and return the day name for that date.
    Each day must be one of the following strings: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday.
    For example, the day name for the date 12/07/2016 is Wednesday.
 */

function getDayName(dateString) {
    const date = new Date(dateString);
    const day_names = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
    };
    return day_names[date.getDay()];
}
