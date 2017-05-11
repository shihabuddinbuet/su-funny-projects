package com.ipv.su.udedis.dao;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisCluster;
import redis.clients.jedis.JedisPool;

public class RedisDaoImpl implements RedisDao{
	private final String DEFAULT_PATTERN = "*";
	private final JedisCluster connection = RedisManager.getConnection();
	
	@Override
	public Set<String> getKeys() {
		Set<String> keys = new HashSet<String>();
		List<Jedis> connections = getPerNodeConnection(connection);
		for (Jedis jedis : connections) {
			keys.addAll(getKeysByNode(jedis, DEFAULT_PATTERN));
		}
		return keys;
	}
	
	private List<Jedis> getPerNodeConnection(JedisCluster clusterConnection) {
		List<Jedis> connections = new ArrayList<Jedis>();
		Map<String, JedisPool> nodes = clusterConnection.getClusterNodes();
		for (Map.Entry<String, JedisPool> node : nodes.entrySet()) {
			Jedis connection = node.getValue().getResource();
			connections.add(connection);
		}
		return connections;
	}
	
	private Set<String> getKeysByNode(Jedis connection, String pattern) {
		return connection.keys(pattern);
	}
	
}
