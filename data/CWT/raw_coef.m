clearvars; close all; clc;

%% File's directory and the list of file names

path = '../audionorm/';
%path = '../audio/';
svpath = 'coefzdr/';
%svpath = 'coefzdrun/';

files = dir(path);
files = rmfield(files, 'folder');
files = rmfield(files, 'bytes');
files = rmfield(files, 'datenum');
files = rmfield(files, 'isdir');
files = rmfield(files, 'date');
files(1:2) = [];
files = {files.name}.';

%% Get raw coefficients


for i=1:length(files)
    disp(['Get raw coefficients in ' files{i,1}]);
    load([path files{i}]);
    fs = double(fs);
    rawcoef = cwt(newau,20:200,'db2',1/fs);
    save([svpath files{i}],'rawcoef','-v7');
end

%{
for i=1:length(files)
    disp(['Get raw coefficients in ' files{i,1}]);
    [au,fs] = audioread([path files{i}]);
    rawcoef = cwt(au,20:200,'morl',1/fs);
    save([svpath files{i} '.mat'],'rawcoef','-v7');
end
%}