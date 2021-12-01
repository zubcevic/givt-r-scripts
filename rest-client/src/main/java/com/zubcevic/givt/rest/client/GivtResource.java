package com.zubcevic.givt.rest.client;

import java.util.Set;

import javax.inject.Inject;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;

import com.zubcevic.givt.rest.client.GivtService.CollectGroup;
import org.eclipse.microprofile.rest.client.inject.RestClient;

@Path("/givt")
public class GivtResource {


    @Inject
    @RestClient
    GivtService remoteService;

    @GET
    @Path("/id/{id}")
    public Set<CollectGroup> id(@PathParam("id") String id) {
        System.out.println(id);
        return remoteService.getCollectGroup();
    }
}