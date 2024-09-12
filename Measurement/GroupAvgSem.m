function [avg,sem] = GroupAvgSem(data,tags, tagOptions)
% computes avg and sem based on group
numGroups = length(tagOptions);

for pos = 1:numGroups
    idx = tags == tagOptions(pos);
    thisData = data(idx);
    avg(pos, 1) = mean(thisData,1);
    STD(pos, 1) = std(thisData,[],1);
    sem(pos, 1) = std(thisData,[],1)./sqrt(length(idx));    

end


end