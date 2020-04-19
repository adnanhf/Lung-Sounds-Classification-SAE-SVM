clearvars; close all; clc;

%% File's directory and the list of file names

path = '../audionorm/';
%path = '../audio/';
svpath = 'wavedec/';
%svpath = 'wavedecun/';

files = dir(path);
files = rmfield(files, 'folder');
files = rmfield(files, 'bytes');
files = rmfield(files, 'datenum');
files = rmfield(files, 'isdir');
files = rmfield(files, 'date');
files(1:2) = [];
files = {files.name}.';

%% Get raw coefficients

%% Mother Wavelet: DB2


for i=1:length(files)
    disp(['Acquire decomposition db2 order 7 in ' files{i,1}]);
    load([path files{i}]);
    [coef,leng] = wavedec(newau,7,'db2');
    %save([svpath '7kanhadb2' files{i}], 'coef', 'leng', '-v7');
end

%{
for i=1:length(files)
    disp(['Acquire decomposition db2 order 7 in ' files{i,1}]);
    [au,~] = audioread([path files{i}]);
    [coef,leng] = wavedec(au,7,'db2');
    save([svpath '7kanhadb2-unpre' files{i} '.mat'], 'coef', 'leng', '-v7');
end
%}