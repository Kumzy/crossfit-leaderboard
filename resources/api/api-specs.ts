export namespace API {
    export namespace AccountLogin {
        export namespace Http201 {
            export type ResponseBody = {
                access_token: string;
                expires_in ? : null | number;
                refresh_token ? : null | string;
                token_type: string;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export type RequestBody = {
            password: string;
            username: string;
        };
    };

    export namespace AccountLogout {
        export namespace Http201 {
            export type ResponseBody = {

            };
        };
    };

    export namespace AccountProfile {
        export namespace Http200 {
            export type ResponseBody = {
                email: string;
                id: string;
                isActive ? : boolean;
                isSuperuser ? : boolean;
                isVerified ? : boolean;
                name ? : null | string;
                oauthAccounts ? : {
                    accessToken: string;
                    accountEmail: string;
                    accountId: string;
                    expiresAt ? : null | number;
                    id: string;
                    oauthName: string;
                    refreshToken ? : null | string;
                } [];
                roles ? : {
                    assignedAt: string;
                    roleId: string;
                    roleName: string;
                    roleSlug: string;
                } [];
                teams ? : {
                    isOwner ? : boolean;
                    role ? : "CAPTAIN" | "MEMBER";
                    teamId: string;
                    teamName: string;
                } [];
            };
        };
    };

    export namespace AccountRegister {
        export namespace Http201 {
            export type ResponseBody = {
                email: string;
                id: string;
                isActive ? : boolean;
                isSuperuser ? : boolean;
                isVerified ? : boolean;
                name ? : null | string;
                oauthAccounts ? : {
                    accessToken: string;
                    accountEmail: string;
                    accountId: string;
                    expiresAt ? : null | number;
                    id: string;
                    oauthName: string;
                    refreshToken ? : null | string;
                } [];
                roles ? : {
                    assignedAt: string;
                    roleId: string;
                    roleName: string;
                    roleSlug: string;
                } [];
                teams ? : {
                    isOwner ? : boolean;
                    role ? : "CAPTAIN" | "MEMBER";
                    teamId: string;
                    teamName: string;
                } [];
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export type RequestBody = {
            email: string;
            name ? : null | string;
            password: string;
        };
    };

    export namespace AddMemberToTeam {
        export namespace Http201 {
            export type ResponseBody = {
                description ? : null | string;
                id: string;
                members ? : {
                    email: string;
                    id: string;
                    isOwner ? : boolean | null;
                    name ? : null | string;
                    role ? : "CAPTAIN" | "MEMBER" | null;
                    userId: string;
                } [];
                name: string;
                tags ? : {
                    id: string;
                    name: string;
                    slug: string;
                } [];
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            team_id: string;
        };

        export type RequestBody = {
            userName: string;
        };
    };

    export namespace AssignUserRole {
        export namespace Http201 {
            export type ResponseBody = {
                message: string;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            role_slug: string;
        };

        export type RequestBody = {
            userName: string;
        };
    };

    export namespace CreateCompetition {
        export namespace Http201 {
            export type ResponseBody = {
                description ? : null | string;
                id: string;
                name ? : null | string;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export type RequestBody = {
            dateEnd ? : null | string;
            dateStart ? : null | string;
            description ? : null | string;
            name: string;
        };
    };

    export namespace CreateDivision {
        export namespace Http201 {
            export type ResponseBody = {
                competitionId: string;
                description ? : null | string;
                divisionScoringType ? : "POINT" | "RANK";
                id: string;
                isTeam: boolean;
                name: string;
                teamSize ? : null | number;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export type RequestBody = {
            competitionId: string;
            description ? : null | string;
            divisionScoringType ? : "POINT" | "RANK";
            isTeam ? : boolean;
            name: string;
            teamSize ? : null | number;
        };
    };

    export namespace CreateTag {
        export namespace Http201 {
            export type ResponseBody = {
                description ? : null | string;
                id ? : string;
                name: string;
                slug: string;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export type RequestBody = {
            description ? : null | string;
            name: string;
            slug: string;
        };
    };

    export namespace CreateTeam {
        export namespace Http201 {
            export type ResponseBody = {
                description ? : null | string;
                id: string;
                members ? : {
                    email: string;
                    id: string;
                    isOwner ? : boolean | null;
                    name ? : null | string;
                    role ? : "CAPTAIN" | "MEMBER" | null;
                    userId: string;
                } [];
                name: string;
                tags ? : {
                    id: string;
                    name: string;
                    slug: string;
                } [];
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export type RequestBody = {
            description ? : null | string;
            name: string;
            tags ? : string[];
        };
    };

    export namespace CreateUser {
        export namespace Http201 {
            export type ResponseBody = {
                email: string;
                id: string;
                isActive ? : boolean;
                isSuperuser ? : boolean;
                isVerified ? : boolean;
                name ? : null | string;
                oauthAccounts ? : {
                    accessToken: string;
                    accountEmail: string;
                    accountId: string;
                    expiresAt ? : null | number;
                    id: string;
                    oauthName: string;
                    refreshToken ? : null | string;
                } [];
                roles ? : {
                    assignedAt: string;
                    roleId: string;
                    roleName: string;
                    roleSlug: string;
                } [];
                teams ? : {
                    isOwner ? : boolean;
                    role ? : "CAPTAIN" | "MEMBER";
                    teamId: string;
                    teamName: string;
                } [];
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export type RequestBody = {
            email: string;
            isActive ? : boolean;
            isSuperuser ? : boolean;
            isVerified ? : boolean;
            name ? : null | string;
            password: string;
        };
    };

    export namespace DeleteCompetition {
        export namespace Http204 {
            export type ResponseBody = undefined;
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            competition_id: string;
        };
    };

    export namespace DeleteDivision {
        export namespace Http204 {
            export type ResponseBody = undefined;
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            competition_id: string;
            division_id: string;
        };
    };

    export namespace DeleteTag {
        export namespace Http204 {
            export type ResponseBody = undefined;
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            tag_id: string;
        };
    };

    export namespace DeleteTeam {
        export namespace Http204 {
            export type ResponseBody = undefined;
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            team_id: string;
        };
    };

    export namespace DeleteUser {
        export namespace Http204 {
            export type ResponseBody = undefined;
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            user_id: string;
        };
    };

    export namespace GetCompetition {
        export namespace Http200 {
            export type ResponseBody = {
                description ? : null | string;
                id: string;
                name ? : null | string;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            competition_id: string;
        };
    };

    export namespace GetDivision {
        export namespace Http200 {
            export type ResponseBody = {
                competitionId: string;
                description ? : null | string;
                divisionScoringType ? : "POINT" | "RANK";
                id: string;
                isTeam: boolean;
                name: string;
                teamSize ? : null | number;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            competition_id: string;
            division_id: string;
        };
    };

    export namespace GetTag {
        export namespace Http200 {
            export type ResponseBody = {
                description ? : null | string;
                id ? : string;
                name: string;
                slug: string;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            tag_id: string;
        };
    };

    export namespace GetTeam {
        export namespace Http200 {
            export type ResponseBody = {
                description ? : null | string;
                id: string;
                members ? : {
                    email: string;
                    id: string;
                    isOwner ? : boolean | null;
                    name ? : null | string;
                    role ? : "CAPTAIN" | "MEMBER" | null;
                    userId: string;
                } [];
                name: string;
                tags ? : {
                    id: string;
                    name: string;
                    slug: string;
                } [];
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            team_id: string;
        };
    };

    export namespace GetUser {
        export namespace Http200 {
            export type ResponseBody = {
                email: string;
                id: string;
                isActive ? : boolean;
                isSuperuser ? : boolean;
                isVerified ? : boolean;
                name ? : null | string;
                oauthAccounts ? : {
                    accessToken: string;
                    accountEmail: string;
                    accountId: string;
                    expiresAt ? : null | number;
                    id: string;
                    oauthName: string;
                    refreshToken ? : null | string;
                } [];
                roles ? : {
                    assignedAt: string;
                    roleId: string;
                    roleName: string;
                    roleSlug: string;
                } [];
                teams ? : {
                    isOwner ? : boolean;
                    role ? : "CAPTAIN" | "MEMBER";
                    teamId: string;
                    teamName: string;
                } [];
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            user_id: string;
        };
    };

    export namespace ListCompetitions {
        export namespace Http200 {
            export type ResponseBody = {
                items: {
                    description ? : null | string;
                    id: string;
                    name ? : null | string;
                } [];
                limit: number;
                offset: number;
                total: number;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface QueryParameters {
            createdAfter ? : null | string;
            createdBefore ? : null | string;
            currentPage ? : number;
            ids ? : null | string[];
            orderBy ? : null | string;
            pageSize ? : number;
            searchField ? : null | string;
            searchIgnoreCase ? : boolean | null;
            searchString ? : null | string;
            sortOrder ? : "asc" | "desc" | null;
            updatedAfter ? : null | string;
            updatedBefore ? : null | string;
        };
    };

    export namespace ListDivisions {
        export namespace Http200 {
            export type ResponseBody = {
                items: {
                    competitionId: string;
                    description ? : null | string;
                    divisionScoringType ? : "POINT" | "RANK";
                    id: string;
                    isTeam: boolean;
                    name: string;
                    teamSize ? : null | number;
                } [];
                limit: number;
                offset: number;
                total: number;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            competition_id: string;
        };

        export interface QueryParameters {
            createdAfter ? : null | string;
            createdBefore ? : null | string;
            currentPage ? : number;
            ids ? : null | string[];
            orderBy ? : null | string;
            pageSize ? : number;
            searchField ? : null | string;
            searchIgnoreCase ? : boolean | null;
            searchString ? : null | string;
            sortOrder ? : "asc" | "desc" | null;
            updatedAfter ? : null | string;
            updatedBefore ? : null | string;
        };
    };

    export namespace ListTags {
        export namespace Http200 {
            export type ResponseBody = {
                items: {
                    description ? : null | string;
                    id ? : string;
                    name: string;
                    slug: string;
                } [];
                limit: number;
                offset: number;
                total: number;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface QueryParameters {
            createdAfter ? : null | string;
            createdBefore ? : null | string;
            currentPage ? : number;
            ids ? : null | string[];
            orderBy ? : null | string;
            pageSize ? : number;
            searchField ? : null | string;
            searchIgnoreCase ? : boolean | null;
            searchString ? : null | string;
            sortOrder ? : "asc" | "desc" | null;
            updatedAfter ? : null | string;
            updatedBefore ? : null | string;
        };
    };

    export namespace ListTeams {
        export namespace Http200 {
            export type ResponseBody = {
                items: {
                    description ? : null | string;
                    id: string;
                    members ? : {
                        email: string;
                        id: string;
                        isOwner ? : boolean | null;
                        name ? : null | string;
                        role ? : "CAPTAIN" | "MEMBER" | null;
                        userId: string;
                    } [];
                    name: string;
                    tags ? : {
                        id: string;
                        name: string;
                        slug: string;
                    } [];
                } [];
                limit: number;
                offset: number;
                total: number;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface QueryParameters {
            createdAfter ? : null | string;
            createdBefore ? : null | string;
            currentPage ? : number;
            ids ? : null | string[];
            orderBy ? : null | string;
            pageSize ? : number;
            searchField ? : null | string;
            searchIgnoreCase ? : boolean | null;
            searchString ? : null | string;
            sortOrder ? : "asc" | "desc" | null;
            updatedAfter ? : null | string;
            updatedBefore ? : null | string;
        };
    };

    export namespace ListUsers {
        export namespace Http200 {
            export type ResponseBody = {
                items: {
                    email: string;
                    id: string;
                    isActive ? : boolean;
                    isSuperuser ? : boolean;
                    isVerified ? : boolean;
                    name ? : null | string;
                    oauthAccounts ? : {
                        accessToken: string;
                        accountEmail: string;
                        accountId: string;
                        expiresAt ? : null | number;
                        id: string;
                        oauthName: string;
                        refreshToken ? : null | string;
                    } [];
                    roles ? : {
                        assignedAt: string;
                        roleId: string;
                        roleName: string;
                        roleSlug: string;
                    } [];
                    teams ? : {
                        isOwner ? : boolean;
                        role ? : "CAPTAIN" | "MEMBER";
                        teamId: string;
                        teamName: string;
                    } [];
                } [];
                limit: number;
                offset: number;
                total: number;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface QueryParameters {
            createdAfter ? : null | string;
            createdBefore ? : null | string;
            currentPage ? : number;
            ids ? : null | string[];
            orderBy ? : null | string;
            pageSize ? : number;
            searchField ? : null | string;
            searchIgnoreCase ? : boolean | null;
            searchString ? : null | string;
            sortOrder ? : "asc" | "desc" | null;
            updatedAfter ? : null | string;
            updatedBefore ? : null | string;
        };
    };

    export namespace RemoveMemberFromTeam {
        export namespace Http201 {
            export type ResponseBody = {
                description ? : null | string;
                id: string;
                members ? : {
                    email: string;
                    id: string;
                    isOwner ? : boolean | null;
                    name ? : null | string;
                    role ? : "CAPTAIN" | "MEMBER" | null;
                    userId: string;
                } [];
                name: string;
                tags ? : {
                    id: string;
                    name: string;
                    slug: string;
                } [];
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            team_id: string;
        };

        export type RequestBody = {
            userName: string;
        };
    };

    export namespace RevokeUserRole {
        export namespace Http201 {
            export type ResponseBody = {
                message: string;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            role_slug: string;
        };

        export type RequestBody = {
            userName: string;
        };
    };

    export namespace SystemHealth {
        export namespace Http200 {
            export type ResponseBody = {
                app ? : string;
                cache_status: "offline" | "online";
                database_status: "offline" | "online";
                version ? : string;
                worker_status: "offline" | "online";
            };
        };
    };

    export namespace UpdateCompetition {
        export namespace Http200 {
            export type ResponseBody = {
                description ? : null | string;
                id: string;
                name ? : null | string;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            competition_id: string;
        };

        export type RequestBody = {
            dateEnd: null | string;
            dateStart: null | string;
            description: null | string;
            name: null | string;
        };
    };

    export namespace UpdateDivision {
        export namespace Http200 {
            export type ResponseBody = {
                competitionId: string;
                description ? : null | string;
                divisionScoringType ? : "POINT" | "RANK";
                id: string;
                isTeam: boolean;
                name: string;
                teamSize ? : null | number;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            competition_id: string;
            division_id: string;
        };

        export type RequestBody = {
            description: null | string;
            name: null | string;
            teamSize: null | number;
        };
    };

    export namespace UpdateTag {
        export namespace Http200 {
            export type ResponseBody = {
                description ? : null | string;
                id ? : string;
                name: string;
                slug: string;
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            tag_id: string;
        };

        export type RequestBody = {
            description: null | string;
            name: string;
            slug: string;
        };
    };

    export namespace UpdateTeam {
        export namespace Http200 {
            export type ResponseBody = {
                description ? : null | string;
                id: string;
                members ? : {
                    email: string;
                    id: string;
                    isOwner ? : boolean | null;
                    name ? : null | string;
                    role ? : "CAPTAIN" | "MEMBER" | null;
                    userId: string;
                } [];
                name: string;
                tags ? : {
                    id: string;
                    name: string;
                    slug: string;
                } [];
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            team_id: string;
        };

        export type RequestBody = {
            description: null | string;
            name: null | string;
            tags: null | string[];
        };
    };

    export namespace UpdateUser {
        export namespace Http200 {
            export type ResponseBody = {
                email: string;
                id: string;
                isActive ? : boolean;
                isSuperuser ? : boolean;
                isVerified ? : boolean;
                name ? : null | string;
                oauthAccounts ? : {
                    accessToken: string;
                    accountEmail: string;
                    accountId: string;
                    expiresAt ? : null | number;
                    id: string;
                    oauthName: string;
                    refreshToken ? : null | string;
                } [];
                roles ? : {
                    assignedAt: string;
                    roleId: string;
                    roleName: string;
                    roleSlug: string;
                } [];
                teams ? : {
                    isOwner ? : boolean;
                    role ? : "CAPTAIN" | "MEMBER";
                    teamId: string;
                    teamName: string;
                } [];
            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            user_id: string;
        };

        export type RequestBody = {
            email: null | string;
            isActive: boolean | null;
            isSuperuser: boolean | null;
            isVerified: boolean | null;
            name: null | string;
            password: null | string;
        };
    };

    export namespace WorkerJobAbort {
        export namespace Http202 {
            export type ResponseBody = {

            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            job_id: string;
            queue_id: string;
        };
    };

    export namespace WorkerJobDetail {
        export namespace Http200 {
            export type ResponseBody = {

            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            job_id: string;
            queue_id: string;
        };
    };

    export namespace WorkerJobRetry {
        export namespace Http202 {
            export type ResponseBody = {

            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            job_id: string;
            queue_id: string;
        };
    };

    export namespace WorkerQueueDetail {
        export namespace Http200 {
            export type ResponseBody = {

            };
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface PathParameters {
            queue_id: string;
        };
    };

    export namespace WorkerQueueList {
        export namespace Http200 {
            export type ResponseBody = {

            };
        };
    };
};
