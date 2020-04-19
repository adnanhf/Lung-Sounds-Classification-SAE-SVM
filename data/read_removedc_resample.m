clearvars; close all; clc;

%% Listing files name

zdfiles = dir('audio/');
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
    [au,~] = audioread(['audio/' zdfiles{i,1}]);
    
    audiowrite(['audio8/' zdfiles{i,1}],au,8000);
    
    DCr = dsp.DCBlocker('Algorithm','Subtract mean');
    
    [au,fs] = audioread(['audio8/' zdfiles{i,1}]);
    newau = DCr(au);
    
    save(['audiomat/' zdfiles{i,1} '.mat'], 'newau', 'fs', '-v7');
end