clearvars; close all; clc;

%% Listing files name

zdfiles = dir('zolddata/');
zdfiles = rmfield(zdfiles, 'folder');
zdfiles = rmfield(zdfiles, 'bytes');
zdfiles = rmfield(zdfiles, 'datenum');
zdfiles = rmfield(zdfiles, 'isdir');
zdfiles = rmfield(zdfiles, 'date');
zdfiles(1:2) = [];
zdfiles = {zdfiles.name}.';

%% Read audio files

for i=1:length(zdfiles)
    disp(['Reading audio signal in ' zdfiles{i,1}]);
    [au,fs] = audioread(['zolddata/' zdfiles{i,1}]);
    save(['audiozd/' zdfiles{i,1} '.mat'], 'au', 'fs', '-v7.3');
end