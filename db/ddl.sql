create table frame
(
    id text,
    cam_id text,
    filename text,
    frame int,
    time_stamp timestamp,
    event_time_stamp timestamp,
    local_filename text
);

create table clip (
    id serial,
    clip_start timestamp,
    clip_end timestamp,
    nframes int
);

create table clip_frame (
    clip_id int,
    frame_id text
);
