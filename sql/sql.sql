CREATE TABLE Users (
    NetId VarChar(8) Primary Key,
    UIN   Char(9) Not Null
);

CREATE TABLE Company (
    Name  VarChar(50) Primary Key,
    Descr Text,
    Stack Text,
    Logo  Text
);

CREATE TABLE UserDetails (
    NetId     VarChar(8) Primary Key,
    FirstName VarChar(50) Not Null,
    LastName  VarChar(50) Not Null,
    Phone     VarChar(50),
    BestEmail VarChar(200),
    Picture   VarChar(200) Not Null,
    Github    VarChar(50),
    Euler     VarChar(50),
    Major     VarChar(50),
    Year      Char(20),
    Skills    Text,
    Wants     Text,
    Foreign Key (NetId) References Users(NetId)
);

CREATE TABLE Student (
    NetId VarChar(8) Primary Key,
    Role  VarChar(50),
    Foreign Key (NetId) References Users(NetId)
);

CREATE TABLE Staff (
    NetId VarChar(8) Primary Key,
    Role  VarChar(50),
    Foreign Key (NetId) References Users(NetId)
);

CREATE TABLE Volunteer (
    NetId VarChar(8) Primary Key,
    Role  VarChar(50),
    Foreign Key (NetId) References Users(NetId)
);

CREATE TABLE Team (
    Name    VarChar(50),
    Company VarChar(50),
    Descr   Text,
    Primary Key (Name),
    Foreign Key (Company) References Company(Name)
);

CREATE TABLE TeamMembers (
    NetId   VarChar(8),
    Team    VarChar(50),
    Company VarChar(50),
    Title   VarChar(50),
    Primary Key (NetId, Team, Company),
    Foreign Key (Company) References Company(Name),
    Foreign Key (Team) References Team(Name),
    Foreign Key (NetId)   References Users(NetId)
);

CREATE TABLE TeamStaff (
    NetId   VarChar(8),
    Name    VarChar(50),
    Company VarChar(50),
    Title   VarChar(50),
    Primary Key (NetId, Name, Company),
    Foreign Key (NetId)   References Users(NetId),
    Foreign Key (Company) References Company(Name)
);

CREATE TABLE SponsorCompany (
    Name    VarChar(50) Primary Key,
    Email   VarChar(200),
    Phone   VarChar(50),
    Picture VarChar(200)
);

CREATE TABLE Sponsor (
    FirstName VarChar(50) Not Null,
    LastName  VarChar(50) Not Null,
    Company   VarChar(50),
    WorkEmail VarChar(200),
    Email     VarChar(200),
    Phone     VarChar(50),
    Picture   VarChar(200),
    Primary Key (FirstName, LastName, Company),
    Foreign Key (Company) References SponsorCompany(Name)
);

# Not settled on a clean method yet for meeting recording
CREATE TABLE CAMeeting (
    Id        Integer Unsigned Primary Key Auto_Increment,
    Name      VarChar(50),
    StartDate Date,
    EndDate   Date,
    StartTime VarChar(5),
    EndTime   VarChar(5)
);

CREATE TABLE CAMeetingAttendance (
    MeetingId Integer Unsigned Primary Key Auto_Increment,
    Id        Integer Unsigned,
    NetId     VarChar(8),
    Now       Date,
    Stamp     Integer
);

CREATE TABLE MeetingAttendance (
    MeetingId Integer Unsigned Primary Key Auto_Increment,
    Id        Integer Unsigned,
    NetId     VarChar(8),
    Now       Date,
    Stamp     Integer
);

CREATE TABLE TaskTag (
    Company VarChar(50),
    Name    VarChar(30),
    Primary Key (Company, Name),
    Foreign Key (Company) References Company(Name)
);

CREATE TABLE Task (
    TaskId        Integer Unsigned Primary Key Auto_Increment,
    Company       VarChar(50),
    Tag           VarChar(30),
	Name          VarChar(50),
    CreateTime    Integer Unsigned,
    EndTime       Integer Unsigned,
    Descr         Text,
    Status        Integer,
    Priority      Integer,
    Ease          Integer,
    AssignedUser  VarChar(8),
    CompletedUser VarChar(8),
    Foreign Key (AssignedUser) References Users(NetID),
    Foreign Key (CompletedUser) References Users(NetID),
    Foreign Key (Company, Tag) References TaskTag(Company, Name),
    Foreign Key (Company) References Company(Name)
);
